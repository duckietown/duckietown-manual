#!/usr/bin/env python3

from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import quote

HTML_DIR = Path("html")
BASE_URL = "https://docs.duckietown.com/ente/duckietown-manual/"

EXCLUDE_PARTS = {
    "genindex",
    "search",
    "_sources",
    "_static",
    "_images",
}

def clean_text(text: str) -> str:
    return " ".join(text.split())

def page_url(path: Path) -> str:
    rel = path.relative_to(HTML_DIR).as_posix()
    return BASE_URL + quote(rel)

def should_skip(path: Path) -> bool:
    s = path.as_posix()
    return any(part in s for part in EXCLUDE_PARTS)

def extract_page(path: Path):
    soup = BeautifulSoup(path.read_text(encoding="utf-8", errors="ignore"), "html.parser")

    title = soup.find("h1")
    if title:
        title_text = clean_text(title.get_text(" "))
    elif soup.title:
        title_text = clean_text(soup.title.get_text(" "))
    else:
        title_text = path.stem

    main = soup.find("main") or soup.find("article") or soup.body
    if not main:
        return None

    # Remove noisy elements
    for tag in main(["script", "style", "nav", "footer"]):
        tag.decompose()

    text = clean_text(main.get_text(" "))
    if len(text) < 200:
        return None

    summary = text[:280].rstrip()
    if len(text) > 280:
        summary += "..."

    return {
        "title": title_text,
        "url": page_url(path),
        "summary": summary,
        "text": text,
    }

def main():
    pages = []

    for path in sorted(HTML_DIR.rglob("*.html")):
        if should_skip(path):
            continue
        page = extract_page(path)
        if page:
            pages.append(page)

    llms = []
    llms.append("# Duckietown Manual")
    llms.append("")
    llms.append("> Technical documentation for Duckietown: robot autonomy education, Duckiebot setup, Duckietown software, simulations, learning experiences, and troubleshooting.")
    llms.append("")
    llms.append("This file helps language models and AI coding assistants find the most relevant Duckietown documentation pages.")
    llms.append("")
    llms.append("## Documentation pages")
    llms.append("")

    for page in pages:
        llms.append(f"- [{page['title']}]({page['url']}): {page['summary']}")

    (HTML_DIR / "llms.txt").write_text("\n".join(llms) + "\n", encoding="utf-8")

    full = []
    full.append("# Duckietown Manual — Full LLM Context")
    full.append("")
    full.append("> Expanded plain-text version of the Duckietown Manual for language models.")
    full.append("")

    for page in pages:
        full.append(f"## {page['title']}")
        full.append("")
        full.append(f"URL: {page['url']}")
        full.append("")
        full.append(page["text"])
        full.append("")

    (HTML_DIR / "llms-full.txt").write_text("\n".join(full), encoding="utf-8")

    print(f"Wrote {HTML_DIR / 'llms.txt'}")
    print(f"Wrote {HTML_DIR / 'llms-full.txt'}")
    print(f"Included {len(pages)} pages")

if __name__ == "__main__":
    main()