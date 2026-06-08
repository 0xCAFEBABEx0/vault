#!/usr/bin/env python3
"""Nightly GenAI research collector for this Obsidian/Zettelkasten vault.

Design goals:
- Low token / no LLM dependency: uses arXiv Atom, Semantic Scholar JSON, and RSS/Atom.
- Writes concise literature notes under 2-Literature/ following the vault's existing style.
- Deduplicates by source URL / arXiv ID / existing filenames.
- Optionally commits and pushes changes.
"""
from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
LIT_DIR = ROOT / "2-Literature"
STATE_DIR = ROOT / ".collector-state"
STATE_FILE = STATE_DIR / "nightly_genai_seen.json"

ARXIV_NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

# Keep the search focused to avoid flooding the vault.
ARXIV_QUERIES = [
    'cat:cs.CL AND (all:"large language model" OR all:"language model" OR all:LLM OR all:transformer)',
    'cat:cs.AI AND (all:"generative AI" OR all:"foundation model" OR all:"agent" OR all:"reasoning")',
    'cat:cs.LG AND (all:"diffusion model" OR all:"multimodal" OR all:"retrieval augmented generation" OR all:RAG)',
]

TECH_BLOG_FEEDS = [
    {"name": "OpenAI News", "feed": "https://openai.com/news/rss.xml", "home": "https://openai.com/news/", "source_tag": "source/openai"},
    {"name": "Google DeepMind Blog", "feed": "https://deepmind.google/blog/rss.xml", "home": "https://deepmind.google/blog/", "source_tag": "source/deepmind"},
    # Anthropic and Meta AI currently do not expose stable official RSS endpoints here;
    # do not keep dead URLs in the nightly path.
    {"name": "Microsoft Research Blog", "feed": "https://www.microsoft.com/en-us/research/feed/", "home": "https://www.microsoft.com/en-us/research/blog/", "source_tag": "source/microsoft"},
    {"name": "Hugging Face Blog", "feed": "https://huggingface.co/blog/feed.xml", "home": "https://huggingface.co/blog", "source_tag": "source/huggingface"},
    {"name": "NVIDIA Technical Blog", "feed": "https://developer.nvidia.com/blog/feed/", "home": "https://developer.nvidia.com/blog/", "source_tag": "source/nvidia"},
]

BLOG_KEYWORDS = [
    "generative ai", "large language", "llm", "foundation model", "agent", "reasoning",
    "multimodal", "diffusion", "rag", "retrieval", "transformer", "inference", "alignment",
    "safety", "eval", "benchmark", "fine-tuning", "post-training", "tool use", "model",
]

PAPER_KEYWORDS = [
    "language model", "llm", "large language", "generative", "foundation model", "transformer",
    "diffusion", "multimodal", "agent", "reasoning", "rag", "retrieval", "alignment",
    "post-training", "fine-tuning", "inference", "benchmark", "evaluation", "safety",
]

@dataclass
class Item:
    kind: str  # paper/blog
    title: str
    source: str
    authors: str = ""
    published: str = ""
    updated: str = ""
    summary: str = ""
    arxiv_id: str = ""
    pdf: str = ""
    categories: list[str] = field(default_factory=list)
    source_name: str = ""
    source_tag: str = ""
    related: list[dict] = field(default_factory=list)


def http_get(url: str, timeout: int = 25) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "LazyHermesGenAICollector/1.0 (+https://github.com/0xCAFEBABEx0/vault)"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def clean_text(s: str | None, limit: int | None = None) -> str:
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    if limit and len(s) > limit:
        return s[: limit - 1].rstrip() + "…"
    return s


def slugify(title: str, max_len: int = 88) -> str:
    s = title.strip().replace("’", "").replace("'", "")
    s = re.sub(r"[\\/:*?\"<>|#\[\]{}]", " ", s)
    s = re.sub(r"\s+", " ", s).strip(" .")
    if not s:
        s = "untitled-" + hashlib.sha1(title.encode()).hexdigest()[:8]
    return s[:max_len].rstrip(" .")


def parse_iso_date(s: str) -> str:
    if not s:
        return ""
    try:
        return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).date().isoformat()
    except Exception:
        try:
            return email.utils.parsedate_to_datetime(s).date().isoformat()
        except Exception:
            return s[:10]


def now_jst() -> dt.datetime:
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=9)))


def load_seen() -> set[str]:
    seen = set()
    if STATE_FILE.exists():
        try:
            seen.update(json.loads(STATE_FILE.read_text()).get("seen", []))
        except Exception:
            pass
    # Existing notes are the real source of truth too.
    for p in LIT_DIR.glob("*.md"):
        txt = p.read_text(errors="ignore")[:5000]
        for m in re.finditer(r'source:\s*"([^"]+)"', txt):
            seen.add(m.group(1))
        for m in re.finditer(r"arxiv\.org/(?:abs|html|pdf)/([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)", txt):
            seen.add("arxiv:" + m.group(1).split("v")[0])
    return seen


def save_seen(seen: Iterable[str]) -> None:
    STATE_DIR.mkdir(exist_ok=True)
    STATE_FILE.write_text(json.dumps({"updated": now_jst().isoformat(), "seen": sorted(set(seen))}, ensure_ascii=False, indent=2))


def arxiv_search(max_per_query: int) -> list[Item]:
    items: list[Item] = []
    for q in ARXIV_QUERIES:
        params = urllib.parse.urlencode({
            "search_query": q,
            "start": 0,
            "max_results": max_per_query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        })
        url = "https://export.arxiv.org/api/query?" + params
        try:
            data = http_get(url)
            root = ET.fromstring(data)
        except Exception as e:
            print(f"WARN arXiv query failed: {q}: {e}", file=sys.stderr)
            continue
        for entry in root.findall("a:entry", ARXIV_NS):
            title = clean_text(entry.findtext("a:title", default="", namespaces=ARXIV_NS))
            summary = clean_text(entry.findtext("a:summary", default="", namespaces=ARXIV_NS), 1800)
            if not title or "withdrawn" in summary.lower():
                continue
            lower = (title + " " + summary).lower()
            if not any(k in lower for k in PAPER_KEYWORDS):
                continue
            arxiv_url = entry.findtext("a:id", default="", namespaces=ARXIV_NS).strip().replace("http://", "https://")
            arxiv_id = arxiv_url.rsplit("/", 1)[-1]
            authors = ", ".join(clean_text(a.findtext("a:name", default="", namespaces=ARXIV_NS)) for a in entry.findall("a:author", ARXIV_NS))
            cats = [c.get("term", "") for c in entry.findall("a:category", ARXIV_NS) if c.get("term")]
            pdf = f"https://arxiv.org/pdf/{arxiv_id}"
            html_url = f"https://arxiv.org/html/{arxiv_id}"
            items.append(Item(
                kind="paper", title=title, source=html_url, authors=authors,
                published=parse_iso_date(entry.findtext("a:published", default="", namespaces=ARXIV_NS)),
                updated=parse_iso_date(entry.findtext("a:updated", default="", namespaces=ARXIV_NS)),
                summary=summary, arxiv_id=arxiv_id, pdf=pdf, categories=cats,
                source_name="arXiv", source_tag="source/arxiv",
                related=[{"title": "arXiv abstract", "url": f"https://arxiv.org/abs/{arxiv_id}"}, {"title": "PDF", "url": pdf}],
            ))
        time.sleep(3.1)  # arXiv polite rate limit
    # Deduplicate by base arXiv ID.
    dedup = {}
    for it in items:
        dedup.setdefault(it.arxiv_id.split("v")[0], it)
    return list(dedup.values())


def semantic_related(arxiv_id: str, limit: int = 5) -> list[dict]:
    base = arxiv_id.split("v")[0]
    url = f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{urllib.parse.quote(base)}/references?" + urllib.parse.urlencode({
        "fields": "title,authors,year,citationCount,externalIds,url,isOpenAccess,openAccessPdf",
        "limit": limit,
    })
    try:
        data = json.loads(http_get(url, timeout=20).decode("utf-8"))
    except Exception as e:
        print(f"WARN Semantic Scholar failed for {arxiv_id}: {e}", file=sys.stderr)
        return []
    out = []
    for row in data.get("data", []):
        p = row.get("citedPaper") or {}
        title = clean_text(p.get("title"), 180)
        if not title:
            continue
        ext = p.get("externalIds") or {}
        link = p.get("url") or ""
        if ext.get("ArXiv"):
            link = f"https://arxiv.org/abs/{ext['ArXiv']}"
        elif (p.get("openAccessPdf") or {}).get("url"):
            link = p["openAccessPdf"]["url"]
        out.append({
            "title": title,
            "url": link,
            "year": p.get("year") or "",
            "citations": p.get("citationCount") or 0,
        })
    return out


def parse_feed_date(entry: ET.Element, ns: dict) -> str:
    for tag in ["published", "updated", "pubDate"]:
        val = entry.findtext(f"a:{tag}", namespaces=ns) or entry.findtext(tag)
        if val:
            return parse_iso_date(val)
    return ""


def extract_html_summary(url: str, limit: int = 1200) -> str:
    """Fetch a page and extract a concise non-LLM summary fallback.

    RSS feeds, especially Hugging Face's, sometimes omit summaries entirely.
    Prefer explicit meta descriptions; fall back to the first substantial
    paragraphs so we do not create empty literature notes.
    """
    try:
        raw = http_get(url, timeout=20).decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"WARN page summary fetch failed for {url}: {e}", file=sys.stderr)
        return ""

    paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", raw, re.I | re.S)
    useful: list[str] = []
    for para in paragraphs:
        text = clean_text(para, 500)
        lower = text.lower()
        if len(text) < 80:
            continue
        if text.startswith("Models Datasets Spaces"):
            continue
        if any(skip in lower for skip in ["subscribe", "cookie", "privacy policy", "terms of service", "more articles from our blog"]):
            continue
        useful.append(text)
        if sum(len(x) for x in useful) >= limit:
            break
    paragraph_summary = clean_text(" ".join(useful), limit)
    if len(paragraph_summary) >= 80:
        return paragraph_summary

    meta_patterns = [
        r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:description["\']',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']description["\']',
    ]
    for pat in meta_patterns:
        m = re.search(pat, raw, re.I | re.S)
        if m:
            text = clean_text(m.group(1), limit)
            if len(text) >= 80 and "advance and democratize artificial intelligence" not in text.lower():
                return text
    return ""


def rss_items(max_total: int) -> list[Item]:
    out: list[Item] = []
    for feed in TECH_BLOG_FEEDS:
        try:
            data = http_get(feed["feed"])
            root = ET.fromstring(data)
        except Exception as e:
            print(f"WARN feed failed: {feed['name']}: {e}", file=sys.stderr)
            continue
        entries = []
        if root.tag.endswith("rss") or root.find("channel") is not None:
            entries = root.findall("./channel/item")
            mode = "rss"
        else:
            entries = root.findall("a:entry", {"a": "http://www.w3.org/2005/Atom"}) or root.findall("entry")
            mode = "atom"
        for e in entries[:12]:
            if mode == "rss":
                title = clean_text(e.findtext("title"))
                link = clean_text(e.findtext("link"))
                desc = clean_text(e.findtext("description") or e.findtext("encoded"), 1200)
                pub = parse_iso_date(e.findtext("pubDate") or "")
            else:
                title = clean_text(e.findtext("a:title", namespaces={"a": "http://www.w3.org/2005/Atom"}) or e.findtext("title"))
                link = ""
                for l in e.findall("a:link", {"a": "http://www.w3.org/2005/Atom"}) + e.findall("link"):
                    href = l.get("href")
                    if href and (not l.get("rel") or l.get("rel") == "alternate"):
                        link = href; break
                desc = clean_text(e.findtext("a:summary", namespaces={"a": "http://www.w3.org/2005/Atom"}) or e.findtext("summary") or e.findtext("a:content", namespaces={"a": "http://www.w3.org/2005/Atom"}), 1200)
                pub = parse_feed_date(e, {"a": "http://www.w3.org/2005/Atom"})
            if title and link and not desc:
                desc = extract_html_summary(link, limit=1200)
            lower = (title + " " + desc).lower()
            if not title or not link or not desc or not any(k in lower for k in BLOG_KEYWORDS):
                continue
            out.append(Item(
                kind="blog", title=title, source=link, authors=feed["name"], published=pub,
                summary=desc, source_name=feed["name"], source_tag=feed["source_tag"],
                related=[{"title": feed["name"], "url": feed["home"]}],
            ))
    # newest-ish first; cap
    out.sort(key=lambda x: x.published or "", reverse=True)
    dedup = {}
    for it in out:
        dedup.setdefault(it.source, it)
    return list(dedup.values())[:max_total]


def keyword_tags(item: Item) -> list[str]:
    text = (item.title + " " + item.summary).lower()
    tags = ["type/literature", "theme/research", "theme/learning"]
    if item.source_tag:
        tags.append(item.source_tag)
    mapping = [
        ("keyword/transformer", ["transformer", "attention"]),
        ("keyword/language-model", ["language model", "llm", "large language"]),
        ("keyword/ai", ["generative ai", "foundation model", "artificial intelligence"]),
        ("keyword/nlp", ["nlp", "language", "text"]),
        ("keyword/multimodal", ["multimodal", "vision-language", "audio", "video"]),
        ("keyword/diffusion", ["diffusion"]),
        ("keyword/retrieval", ["retrieval", "rag"]),
        ("keyword/evaluation", ["evaluation", "eval", "benchmark", "leaderboard"]),
        ("keyword/benchmark", ["benchmark", "leaderboard"]),
        ("keyword/reasoning", ["reasoning", "chain-of-thought"]),
        ("keyword/agents", ["agent", "tool use", "tools"]),
        ("keyword/safety", ["safety", "alignment", "jailbreak", "red team"]),
        ("keyword/machine-learning", ["machine learning", "training", "fine-tuning", "post-training", "inference"]),
        ("keyword/research-paper", ["arxiv", "paper"] if item.kind == "paper" else []),
    ]
    for tag, keys in mapping:
        if keys and any(k in text for k in keys):
            tags.append(tag)
    # preserve order, cap around 12 because existing notes are already keyword-heavy.
    seen = []
    for t in tags:
        if t not in seen:
            seen.append(t)
    return seen[:12]


def write_note(item: Item, dry_run: bool = False) -> Path | None:
    LIT_DIR.mkdir(exist_ok=True)
    fname = slugify(item.title) + ".md"
    path = LIT_DIR / fname
    i = 2
    while path.exists():
        # if same source, don't duplicate
        head = path.read_text(errors="ignore")[:2000]
        if item.source in head or (item.arxiv_id and item.arxiv_id.split("v")[0] in head):
            return None
        path = LIT_DIR / f"{slugify(item.title, 78)}-{i}.md"
        i += 1
    tags = keyword_tags(item)
    created = now_jst().date().isoformat()
    desc = clean_text(item.summary, 420).replace('"', "'")
    author = clean_text(item.authors, 360).replace('"', "'")
    title = item.title.replace('"', "'")
    body = [
        "---",
        f'title: "{title}"',
        f'source: "{item.source}"',
        f'author: "{author}"',
        f'published: "{item.published}"',
        f'created: {created}',
        f'description: "{desc}"',
        "tags:",
    ]
    body.extend([f"  - {t}" for t in tags])
    body.extend([
        "---",
        "",
        f"# {item.title}",
        "",
        "## Source Metadata",
        f"- type:: {item.kind}",
        f"- source:: [{item.source_name or item.kind}]({item.source})",
        f"- published:: {item.published or 'unknown'}",
    ])
    if item.updated:
        body.append(f"- updated:: {item.updated}")
    if item.arxiv_id:
        body.extend([f"- arxiv_id:: {item.arxiv_id}", f"- pdf:: {item.pdf}"])
    if item.categories:
        body.append(f"- categories:: {', '.join(item.categories)}")
    body.extend([
        "",
        "## Abstract / Summary",
        clean_text(item.summary, 1800) or "(No summary provided by source feed.)",
        "",
        "## Why it matters for GenAI tracking",
        "- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.",
        "- Review manually before promoting any idea to `3_Permanent` notes.",
        "",
        "## Related Materials",
    ])
    rels = item.related[:]
    if item.kind == "paper" and item.arxiv_id:
        rels.extend(semantic_related(item.arxiv_id, limit=5))
        time.sleep(1.1)
    seen_rel = set()
    for r in rels:
        url = r.get("url") or ""
        rt = r.get("title") or url
        if not url or url in seen_rel:
            continue
        seen_rel.add(url)
        extra = []
        if r.get("year"):
            extra.append(str(r["year"]))
        if r.get("citations"):
            extra.append(f"citations: {r['citations']}")
        suffix = f" ({', '.join(extra)})" if extra else ""
        body.append(f"- [{rt}]({url}){suffix}")
    body.extend([
        "",
        "## Follow-up Questions",
        "- question:: Should this be converted into a permanent insight note?",
        "- question:: Are there implementation details, benchmarks, or released code worth tracking separately?",
        "",
        "---",
        "Tags: " + " ".join("#" + t for t in tags),
        "",
    ])
    content = "\n".join(body)
    if dry_run:
        print(f"DRY would write: {path.relative_to(ROOT)}")
        return path
    path.write_text(content, encoding="utf-8")
    return path


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=check)


def ensure_git_identity() -> None:
    name = git("config", "user.name", check=False).stdout.strip()
    email = git("config", "user.email", check=False).stdout.strip()
    if not name:
        git("config", "user.name", "Lazy Hermes")
    if not email:
        git("config", "user.email", "lazy-hermes@users.noreply.github.com")


def commit_and_push(files: list[Path], push: bool) -> None:
    if not files:
        print("No new notes to commit.")
        return
    ensure_git_identity()
    git("add", *[str(p.relative_to(ROOT)) for p in files], str(STATE_FILE.relative_to(ROOT)))
    status = git("status", "--short").stdout
    print(status)
    if not status.strip():
        print("No git changes.")
        return
    msg = f"vault backup: nightly genai research {now_jst().strftime('%Y-%m-%d %H:%M:%S JST')}"
    git("commit", "-m", msg)
    print(f"Committed: {msg}")
    if push:
        print(git("push", "origin", "HEAD:main", check=True).stdout)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-papers", type=int, default=int(os.environ.get("GENAI_MAX_PAPERS", "6")))
    ap.add_argument("--max-blogs", type=int, default=int(os.environ.get("GENAI_MAX_BLOGS", "6")))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--push", action="store_true")
    args = ap.parse_args()

    os.chdir(ROOT)
    seen = load_seen()
    candidates: list[Item] = []
    candidates.extend(arxiv_search(max_per_query=max(3, args.max_papers)))
    candidates.extend(rss_items(max_total=args.max_blogs))

    new_files: list[Path] = []
    written_by_kind = {"paper": 0, "blog": 0}
    limits = {"paper": args.max_papers, "blog": args.max_blogs}
    for item in candidates:
        if written_by_kind.get(item.kind, 0) >= limits.get(item.kind, 0):
            continue
        keys = {item.source}
        if item.arxiv_id:
            keys.add("arxiv:" + item.arxiv_id.split("v")[0])
        if any(k in seen for k in keys):
            continue
        p = write_note(item, dry_run=args.dry_run)
        if p:
            new_files.append(p)
            written_by_kind[item.kind] = written_by_kind.get(item.kind, 0) + 1
            seen.update(keys)
            print(f"NEW {item.kind}: {item.title} -> {p.relative_to(ROOT)}")
        if written_by_kind["paper"] >= args.max_papers and written_by_kind["blog"] >= args.max_blogs:
            break
    if not args.dry_run:
        save_seen(seen)
        commit_and_push(new_files, push=args.push)
    else:
        print(f"DRY RUN complete. Candidate new files: {len(new_files)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
