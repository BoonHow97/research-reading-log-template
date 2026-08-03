#!/usr/bin/env python3
"""
search_tags.py — Search across all paper notes in topics/ by tag.

Usage:
    python3 search_tags.py                  # list every tag in use, with counts
    python3 search_tags.py QROM              # find all papers tagged "QROM"
    python3 search_tags.py QROM cs2309       # find papers tagged with ALL of these
    python3 search_tags.py --any QROM cs2309 # find papers tagged with ANY of these

Run this from the repository root (the folder containing topics/).
"""

import re
import sys
from pathlib import Path

TOPICS_DIR = Path("topics")

# Matches \logtags{tag-one, tag-two, tag-three}
TAG_PATTERN = re.compile(r"\\logtags\{([^}]*)\}")
# Matches the paper title from \begin{paperbox}{Title}
TITLE_PATTERN = re.compile(r"\\begin\{paperbox\}\s*\{([^}]*)\}")


def strip_latex_comments(text: str) -> str:
    """Remove LaTeX comment lines (anything after an unescaped %) so commented-out
    example usage (e.g. '% Usage: \\logtags{...}') isn't mistaken for real tags."""
    cleaned_lines = []
    for line in text.split("\n"):
        # Find an unescaped % (not preceded by a backslash)
        match = re.search(r"(?<!\\)%", line)
        if match:
            line = line[: match.start()]
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def parse_file(path: Path):
    """Return (title, [tags]) for a single .tex file, or (None, []) if no tags found."""
    text = strip_latex_comments(path.read_text(encoding="utf-8"))

    tag_match = TAG_PATTERN.search(text)
    if not tag_match or not tag_match.group(1).strip():
        return None, []

    tags = [t.strip() for t in tag_match.group(1).split(",") if t.strip()]

    title_match = TITLE_PATTERN.search(text)
    title = title_match.group(1).strip() if title_match else path.stem

    return title, tags


def scan_repo():
    """Return a list of (filepath, title, [tags]) for every .tex file with tags."""
    if not TOPICS_DIR.exists():
        print(f"Error: '{TOPICS_DIR}/' not found. Run this script from the repo root.")
        sys.exit(1)

    results = []
    for tex_file in sorted(TOPICS_DIR.rglob("*.tex")):
        title, tags = parse_file(tex_file)
        if tags:
            results.append((tex_file, title, tags))
    return results


def list_all_tags(results):
    tag_counts = {}
    for _, _, tags in results:
        for tag in tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    if not tag_counts:
        print("No tags found. Add \\logtags{...} to your paper notes first.")
        return

    print(f"{len(tag_counts)} unique tags across {len(results)} tagged papers:\n")
    for tag, count in sorted(tag_counts.items(), key=lambda x: -x[1]):
        print(f"  {tag:<25} ({count})")


def search(results, query_tags, match_any=False):
    query_set = {t.lower() for t in query_tags}
    matches = []

    for filepath, title, tags in results:
        tag_set = {t.lower() for t in tags}
        hit = (query_set & tag_set) if match_any else (query_set <= tag_set)
        if hit:
            matches.append((filepath, title, tags))

    mode = "ANY" if match_any else "ALL"
    print(f"Papers matching {mode} of {query_tags}:\n")

    if not matches:
        print("  (no matches)")
        return

    for filepath, title, tags in matches:
        print(f"  {filepath}")
        print(f"    Title: {title}")
        print(f"    Tags:  {', '.join(tags)}\n")


def main():
    args = sys.argv[1:]
    results = scan_repo()

    if not args:
        list_all_tags(results)
        return

    match_any = "--any" in args
    query_tags = [a for a in args if a != "--any"]

    if not query_tags:
        print("Provide at least one tag to search for.")
        sys.exit(1)

    search(results, query_tags, match_any=match_any)


if __name__ == "__main__":
    main()