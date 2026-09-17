#!/usr/bin/env python3
"""Audit Markdown and MyST source files in the Duckietown Manual."""

from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE_ROOT = ROOT / "src"
MARKDOWNLINT_COMMAND = ("npx", "--yes", "markdownlint-cli2@0.23.2")
LITERAL_DIRECTIVES = {"code-block", "code-cell", "eval-rst", "literalinclude", "raw"}
RENDERED_FENCE_DELIMITERS = {
    "needget": ("`", 3),
    "testexpect": (":", 3),
    "trouble": ("`", 3),
}
HTML_COMMENT_OPEN = "<!--"
HTML_COMMENT_END_PATTERN = re.compile(r"--!?>")
FENCE_PATTERN = re.compile(r"^\s*(?:(?:[-+*]|\d+[.)])\s+)*(?:-\s+)?(`{3,}|~{3,}|:{3,})(.*)$")
INDENTED_CODE_PATTERN = re.compile(r"^(?:[ \t]*\t| {4,})[ \t]*\S")
INDENTED_INLINE_CODE_PATTERN = re.compile(r"^\s+`[^`\n]+`\s*$")
LIST_ITEM_PATTERN = re.compile(r"^(\s*)([-+*]|\d+[.)])\s+(\S(?:.*\S)?)\s*$")
INCLUDE_PATTERN = re.compile(r"^\{include\}\s+(?P<target>\S+)")
LIST_QUALIFIER_PATTERN = re.compile(r"^(?:\([^)]*\)\s*)+")
SENTENCE_START_PATTERN = re.compile(
    r"^(?:A|An|The|This|That|These|Those|Each|Every|All|Any|Some|No|If|When|While|Once|Before|After|Then|First|Next|Finally|You|Your|It|They|We|Use|Open|Run|Enter|Click|Select|Add|Create|Install|Make|Set|Copy|Start|Stop|Ensure|Verify|Check|Choose|Connect|Download|Navigate|Place|Move|Remove|Press|Restart|Reboot|Type|Follow|Go|Find|Locate|Attach|Turn|Build|Clone|Edit|Save|Pull|Push|Test|Read|Write|Enable|Disable|Configure|Launch|Wait|Repeat|Update|Switch|Generate|Paste|Print|Face|Drive|Measure|Collect|Annotate|Train|Export|Indicate|Communicate|Signal|Express|Light|For|With|Without|From|To|In|On|At|By|As|Note|Important|Warning)\b"
)
PROPER_SUBJECT_PATTERN = re.compile(
    r"^[\"'([{]*[A-Z][A-Za-z0-9-]*(?:\s+[A-Za-z][A-Za-z0-9-]*){0,8}\s+(?:am|are|is|was|were|be|being|been|has|have|had|do|does|did|can|could|will|would|shall|should|may|might|must|allows?|appears?|becomes?|contains?|creates?|depends?|enables?|includes?|installs?|needs?|provides?|requires?|runs?|shows?|starts?|supports?|uses?|works?)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Fence:
    character: str
    length: int
    suffix: str
    directive_name: str | None
    is_directive: bool
    is_literal: bool
    indentation: int


@dataclass(frozen=True)
class CommentSection:
    start: int
    end: int
    open_at: int
    close_at: int
    close_end: int


@dataclass(frozen=True)
class SourceLine:
    source_line: int
    text: str


@dataclass
class RenderedDirectiveFence:
    opening: Fence
    opening_line: SourceLine
    content_lengths: dict[str, int]


@dataclass(frozen=True)
class ListItem:
    indentation: int
    marker: str
    content: str


@dataclass(frozen=True)
class ChildBlock:
    kind: str
    has_preceding_blank: bool


@dataclass(frozen=True)
class Finding:
    file_path: Path
    scope: str
    line: int
    category: str
    detail: str


def display_path(file_path: Path) -> str:
    try:
        return file_path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(file_path)


def markdown_files(requested_files: list[Path]) -> list[Path]:
    files = [file_path.resolve() if file_path.is_absolute() else (ROOT / file_path).resolve() for file_path in requested_files]
    if not files:
        files = sorted(SOURCE_ROOT.rglob("*.md"))

    missing_files = [file_path for file_path in files if not file_path.is_file()]
    if missing_files:
        missing = ", ".join(str(file_path) for file_path in missing_files)
        raise ValueError(f"Markdown source file not found: {missing}")

    invalid_files = [file_path for file_path in files if file_path.suffix != ".md"]
    if invalid_files:
        invalid = ", ".join(str(file_path) for file_path in invalid_files)
        raise ValueError(f"Expected a Markdown source file: {invalid}")

    return files


def read_lines(file_path: Path) -> list[str]:
    return file_path.read_text(encoding="utf-8").split("\n")


def parse_fence(text: str) -> Fence | None:
    match = FENCE_PATTERN.match(text)
    if not match:
        return None

    delimiter, suffix = match.groups()
    directive_match = re.match(r"^\{([^}]+)\}", suffix.lstrip())
    directive_name = directive_match.group(1) if directive_match else None
    indentation = len(text) - len(text.lstrip(" \t"))
    return Fence(
        character=delimiter[0],
        length=len(delimiter),
        suffix=suffix,
        directive_name=directive_name,
        is_directive=directive_name is not None,
        is_literal=directive_name is None or directive_name in LITERAL_DIRECTIVES,
        indentation=indentation,
    )


def closes_fence(fence: Fence, stack: list[Fence]) -> bool:
    if not stack:
        return False
    opening_fence = stack[-1]
    return (
        fence.character == opening_fence.character
        and fence.length >= opening_fence.length
        and not fence.suffix.strip()
    )


def audit_rendered_fence_delimiters(file_path: Path, scope: str, lines: list[SourceLine]) -> list[Finding]:
    findings: list[Finding] = []
    fences: list[Fence] = []
    rendered_directive: RenderedDirectiveFence | None = None
    for line in lines:
        fence = parse_fence(line.text)
        if not fence:
            continue

        if rendered_directive:
            if (
                fence.character == rendered_directive.opening.character
                and fence.length >= rendered_directive.opening.length
                and not fence.suffix.strip()
            ):
                minimum = max(
                    3,
                    rendered_directive.content_lengths.get(rendered_directive.opening.character, 0) + 1,
                )
                marker_name = {"`": "backticks", "~": "tildes", ":": "colons"}[rendered_directive.opening.character]
                if rendered_directive.opening.length > minimum:
                    findings.append(
                        Finding(
                            file_path,
                            scope,
                            rendered_directive.opening_line.source_line,
                            "FENCE_EXCESSIVE_DELIMITERS",
                            f"opening: {rendered_directive.opening.length} {marker_name}; {minimum} are sufficient",
                        )
                    )
                if fence.length > minimum:
                    findings.append(
                        Finding(
                            file_path,
                            scope,
                            line.source_line,
                            "FENCE_EXCESSIVE_DELIMITERS",
                            f"closing: {fence.length} {marker_name}; {minimum} are sufficient",
                        )
                    )
                rendered_directive = None
            else:
                rendered_directive.content_lengths[fence.character] = max(
                    rendered_directive.content_lengths.get(fence.character, 0),
                    fence.length,
                )
            continue

        if closes_fence(fence, fences):
            fences.pop()
        elif (
            not any(open_fence.is_literal for open_fence in fences)
            and fence.directive_name in RENDERED_FENCE_DELIMITERS
        ):
            rendered_directive = RenderedDirectiveFence(fence, line, {})
        else:
            fences.append(fence)
    return findings


def find_comment_end(line: str, start: int = 0) -> tuple[int, int] | None:
    match = HTML_COMMENT_END_PATTERN.search(line, start)
    return match.span() if match else None


def find_comment_sections(lines: list[str]) -> list[CommentSection]:
    sections: list[CommentSection] = []
    fences: list[Fence] = []
    opening: tuple[int, int] | None = None

    for index, line in enumerate(lines):
        if opening:
            comment_end = find_comment_end(line)
            if comment_end:
                close_at, close_end = comment_end
                sections.append(CommentSection(opening[0], index, opening[1], close_at, close_end))
                opening = None
            continue

        fence = parse_fence(line)
        if fence:
            if closes_fence(fence, fences):
                fences.pop()
            else:
                fences.append(fence)
            continue

        open_at = line.find(HTML_COMMENT_OPEN)
        if open_at < 0 or any(open_fence.is_literal for open_fence in fences):
            continue

        comment_end = find_comment_end(line, open_at + len(HTML_COMMENT_OPEN))
        if comment_end:
            close_at, close_end = comment_end
            sections.append(CommentSection(index, index, open_at, close_at, close_end))
        else:
            opening = (index, open_at)

    if opening:
        raise ValueError(f"Unclosed HTML comment at source line {opening[0] + 1}")
    return sections


def find_markdownlint_comment_sections(lines: list[str]) -> list[CommentSection]:
    """Find comments that can be exposed as standalone Markdownlint documents."""
    sections: list[CommentSection] = []
    fences: list[tuple[str, int]] = []
    opening: tuple[int, int] | None = None

    for index, line in enumerate(lines):
        if opening:
            comment_end = find_comment_end(line)
            if comment_end:
                close_at, close_end = comment_end
                sections.append(CommentSection(opening[0], index, opening[1], close_at, close_end))
                opening = None
            continue

        fence_match = re.match(r"^(\s*)(`{3,}|~{3,})(.*)$", line)
        if fence_match:
            delimiter, suffix = fence_match.group(2), fence_match.group(3)
            if fences and delimiter[0] == fences[-1][0] and len(delimiter) >= fences[-1][1] and not suffix.strip():
                fences.pop()
            else:
                fences.append((delimiter[0], len(delimiter)))
            continue

        open_at = line.find(HTML_COMMENT_OPEN)
        if open_at < 0 or fences:
            continue
        comment_end = find_comment_end(line, open_at + len(HTML_COMMENT_OPEN))
        if comment_end:
            close_at, close_end = comment_end
            sections.append(CommentSection(index, index, open_at, close_at, close_end))
        else:
            opening = (index, open_at)

    if opening:
        raise ValueError(f"Unclosed HTML comment at source line {opening[0] + 1}")
    return sections


def active_lines(lines: list[str], sections: list[CommentSection]) -> list[SourceLine]:
    visible = list(lines)
    for section in sections:
        if section.start == section.end:
            line = visible[section.start]
            visible[section.start] = line[: section.open_at] + line[section.close_end :]
            continue

        visible[section.start] = visible[section.start][: section.open_at]
        for index in range(section.start + 1, section.end):
            visible[index] = ""
        visible[section.end] = visible[section.end][section.close_end :]

    return [SourceLine(index + 1, text) for index, text in enumerate(visible)]


def comment_lines(lines: list[str], section: CommentSection) -> list[SourceLine]:
    extracted: list[SourceLine] = []
    for index in range(section.start, section.end + 1):
        original = lines[index]
        start = section.open_at + 4 if index == section.start else 0
        end = section.close_at if index == section.end else len(original)
        text = original[start:end]
        if text.strip() or (index != section.start and index != section.end):
            extracted.append(SourceLine(index + 1, text))
    return extracted


def expose_section(lines: list[str], section: CommentSection) -> str:
    exposed: list[str] = []
    skip_boundary_blank = False

    for index, original in enumerate(lines):
        line = original
        if skip_boundary_blank and not line.strip():
            skip_boundary_blank = False
            continue
        skip_boundary_blank = False

        if index == section.start and re.fullmatch(r"\s*<!--\s*", line):
            skip_boundary_blank = bool(exposed and not exposed[-1].strip() and index + 1 < len(lines) and not lines[index + 1].strip())
            continue
        if index == section.end and re.fullmatch(r"\s*--!?>\s*", line):
            skip_boundary_blank = bool(exposed and not exposed[-1].strip() and index + 1 < len(lines) and not lines[index + 1].strip())
            continue
        if index == section.start:
            line = line[: section.open_at] + line[section.open_at + len(HTML_COMMENT_OPEN) :]
        if index == section.end:
            offset = len(HTML_COMMENT_OPEN) if index == section.start else 0
            line = line[: section.close_at - offset] + line[section.close_end - offset :]
        exposed.append(line)

    return "\n".join(exposed)


def run_markdownlint(files: list[Path]) -> bool:
    print(f"Running Markdownlint on {len(files)} file(s)...")
    command = [*MARKDOWNLINT_COMMAND, *(display_path(file_path) for file_path in files)]
    return subprocess.run(command, cwd=ROOT, check=False).returncode == 0


def check_include_targets(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for file_path in files:
        fences: list[Fence] = []
        for line_number, line in enumerate(read_lines(file_path), start=1):
            fence = parse_fence(line)
            if not fence:
                continue
            if closes_fence(fence, fences):
                fences.pop()
                continue
            if not any(open_fence.is_literal for open_fence in fences) and fence.directive_name == "include":
                target_match = INCLUDE_PATTERN.match(fence.suffix.lstrip())
                if target_match:
                    target = target_match.group("target")
                    if not (file_path.parent / target).resolve().is_file():
                        findings.append(Finding(file_path, "active", line_number, "MISSING_INCLUDE_TARGET", target))
            fences.append(fence)
    return findings


def markdownlint_comments(files: list[Path]) -> tuple[int, list[Finding]]:
    section_count = 0
    findings: list[Finding] = []
    for file_path in files:
        lines = read_lines(file_path)
        for section_index, section in enumerate(find_markdownlint_comment_sections(lines), start=1):
            section_count += 1
            result = subprocess.run(
                [*MARKDOWNLINT_COMMAND, "-"],
                cwd=ROOT,
                input=expose_section(lines, section),
                text=True,
                capture_output=True,
                check=False,
            )
            if result.returncode == 0:
                continue
            output = f"{result.stdout}{result.stderr}"
            diagnostics = "\n".join(
                line
                for line in output.splitlines()
                if not line.startswith(("markdownlint-cli2 ", "Finding:", "Linting:", "Summary:"))
            ).strip()
            findings.append(
                Finding(
                    file_path,
                    f"comment-{section_index}",
                    section.start + 1,
                    "COMMENT_MARKDOWNLINT",
                    diagnostics or "Markdownlint exited nonzero without a diagnostic.",
                )
            )
    return section_count, findings


def parse_list_item(text: str) -> ListItem | None:
    match = LIST_ITEM_PATTERN.match(text)
    if not match:
        return None
    indentation, marker, content = match.groups()
    return ListItem(len(indentation.replace("\t", "    ")), marker, content)


def plain_text(text: str) -> str:
    result = re.sub(r"\{[^}]+\}`[^`]*`", "", text)
    result = re.sub(r"`+[^`]*`+", "", result)
    result = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", result)
    result = re.sub(r"\[\^[^\]]+\]", "", result)
    result = re.sub(r"<[^>]*>", "", result)
    result = re.sub(r"[*_~]", "", result)
    return " ".join(result.split())


def starts_with_lowercase(text: str) -> bool:
    content = LIST_QUALIFIER_PATTERN.sub("", plain_text(text))
    match = re.match(r"^[\"'([{]*([A-Za-z])", content)
    return bool(match and match.group(1).islower())


def has_terminal_punctuation(text: str) -> bool:
    return bool(re.search(r"[.:;?!](?:[\"')\]}]+)?$", plain_text(text)))


def has_terminal_colon(text: str) -> bool:
    return plain_text(text).endswith(":")


def looks_like_sentence(text: str) -> bool:
    content = plain_text(text)
    words = re.findall(r"[A-Za-z]+", content)
    if len(words) < 2 or re.match(r"^(?:https?://|www\.|[-+]?\d)", content):
        return False
    if SENTENCE_START_PATTERN.match(content) or re.match(r"^(?:Power\s+(?:on|off)|Short\s+the)\b", content):
        return True
    return bool(PROPER_SUBJECT_PATTERN.match(content))


def is_structured_list_content(text: str) -> bool:
    content = text.strip()
    return bool(
        re.fullmatch(r"\[[^\]]+\]\([^)]*\)\.?", content)
        or re.match(r"^(?:`|\{[^}]+\}|https?://|www\.|[./~]|--?[A-Za-z]|[A-Za-z][\w.-]*\.(?:md|py|yaml|yml|json|txt|sh))", content)
    )


def first_paragraph(lines: list[SourceLine], index: int, list_item: ListItem) -> str:
    parts = [list_item.content]
    for cursor in range(index + 1, len(lines)):
        line = lines[cursor]
        if (
            not line.text.strip()
            or re.fullmatch(r"\s*---\s*", line.text)
            or parse_fence(line.text)
            or parse_list_item(line.text)
        ):
            break
        indentation = len(line.text) - len(line.text.lstrip(" \t"))
        if indentation < list_item.indentation:
            break
        parts.append(line.text.strip())
    return " ".join(parts)


def child_block(
    lines: list[SourceLine], index: int, list_item: ListItem
) -> ChildBlock | None:
    has_preceding_blank = False
    for cursor in range(index + 1, len(lines)):
        line = lines[cursor]
        if not line.text.strip():
            has_preceding_blank = True
            continue
        indentation = len(line.text) - len(line.text.lstrip(" \t"))
        fence = parse_fence(line.text)
        if fence:
            if indentation > list_item.indentation:
                return ChildBlock(
                    "directive" if fence.is_directive else "code",
                    has_preceding_blank,
                )
            return None
        nested_list = parse_list_item(line.text)
        if nested_list:
            if nested_list.indentation > list_item.indentation:
                return ChildBlock("list", has_preceding_blank)
            return None
        return None
    return None


def rendered_fence_conflict(fence: Fence, open_fences: list[Fence]) -> str | None:
    if not fence.is_literal:
        return None

    for open_fence in reversed(open_fences):
        delimiter = RENDERED_FENCE_DELIMITERS.get(open_fence.directive_name)
        if delimiter and (fence.character, fence.length) == delimiter:
            return open_fence.directive_name
    return None


def rendered_card_directive(open_fences: list[Fence]) -> str | None:
    for open_fence in reversed(open_fences):
        if open_fence.directive_name in RENDERED_FENCE_DELIMITERS:
            return open_fence.directive_name
    return None


def is_indented_code_example(text: str) -> bool:
    return bool(
        INDENTED_CODE_PATTERN.match(text)
        or INDENTED_INLINE_CODE_PATTERN.fullmatch(text)
    )


def audit_list_scope(file_path: Path, scope: str, lines: list[SourceLine], review_unpunctuated: bool) -> list[Finding]:
    findings = audit_rendered_fence_delimiters(file_path, scope, lines)
    fences: list[Fence] = []
    for index, line in enumerate(lines):
        fence = parse_fence(line.text)
        if fence:
            if closes_fence(fence, fences):
                opened = fences.pop()
                next_line = lines[index + 1] if index + 1 < len(lines) else None
                in_table = any(open_fence.directive_name == "list-table" for open_fence in fences)
                in_testexpect = any(open_fence.directive_name == "testexpect" for open_fence in fences)
                if (
                    opened.character == "`"
                    and not in_table
                    and not in_testexpect
                    and next_line
                    and next_line.text.strip()
                    and not parse_fence(next_line.text)
                ):
                    findings.append(Finding(file_path, scope, line.source_line, "FENCE_MISSING_FOLLOWING_BLANK", next_line.text.strip()))
            else:
                previous_line = lines[index - 1] if index else None
                in_literal = any(open_fence.is_literal for open_fence in fences)
                in_table = any(open_fence.directive_name == "list-table" for open_fence in fences)
                in_testexpect = any(open_fence.directive_name == "testexpect" for open_fence in fences)
                if (
                    fence.character == "`"
                    and not in_literal
                    and not in_table
                    and not in_testexpect
                    and previous_line
                    and previous_line.text.strip()
                    and not parse_fence(previous_line.text)
                ):
                    findings.append(Finding(file_path, scope, line.source_line, "FENCE_MISSING_PRECEDING_BLANK", previous_line.text.strip()))
                parent_directive = rendered_fence_conflict(fence, fences)
                if parent_directive:
                    findings.append(
                        Finding(
                            file_path,
                            scope,
                            line.source_line,
                            "RENDERED_FENCE_DELIMITER_CONFLICT",
                            f"{parent_directive}: {line.text.strip()}",
                        )
                    )
                fences.append(fence)
            continue

        if any(open_fence.is_literal for open_fence in fences):
            continue
        if any(open_fence.directive_name == "list-table" for open_fence in fences):
            continue

        parent_directive = rendered_card_directive(fences)
        if parent_directive and is_indented_code_example(line.text):
            findings.append(
                Finding(
                    file_path,
                    scope,
                    line.source_line,
                    "RENDERED_INDENTED_CODE",
                    f"{parent_directive}: {line.text.strip()}",
                )
            )

        list_item = parse_list_item(line.text)
        if not list_item:
            continue
        paragraph = first_paragraph(lines, index, list_item)
        child = child_block(lines, index, list_item)
        in_needget = any(open_fence.directive_name == "needget" for open_fence in fences)
        content_is_structured = is_structured_list_content(list_item.content)
        structured = in_needget or content_is_structured

        if list_item.marker.endswith(")"):
            findings.append(Finding(file_path, scope, line.source_line, "ORDERED_LIST_PARENTHESES", line.text.strip()))
        if list_item.marker in {"*", "+"} and not structured:
            findings.append(Finding(file_path, scope, line.source_line, "NON_DASH_LIST_MARKER", line.text.strip()))
        if not content_is_structured and starts_with_lowercase(paragraph):
            findings.append(Finding(file_path, scope, line.source_line, "LIST_LOWERCASE_START", paragraph))
        if child:
            if not has_terminal_colon(paragraph):
                findings.append(
                    Finding(
                        file_path,
                        scope,
                        line.source_line,
                        "LIST_MISSING_INTRODUCTORY_COLON",
                        f"{paragraph} -> {child.kind}",
                    )
                )
            if child.kind == "list" and not child.has_preceding_blank:
                findings.append(
                    Finding(
                        file_path,
                        scope,
                        line.source_line,
                        "LIST_MISSING_NESTED_LIST_BLANK",
                        paragraph,
                    )
                )
        elif not structured and not has_terminal_punctuation(paragraph):
            if review_unpunctuated or looks_like_sentence(paragraph):
                category = "LIST_UNPUNCTUATED_REVIEW" if review_unpunctuated else "LIST_POSSIBLE_MISSING_TERMINAL_STOP"
                findings.append(Finding(file_path, scope, line.source_line, category, paragraph))
    return findings


def audit_lists_and_fences(files: list[Path], review_unpunctuated: bool) -> tuple[int, list[Finding]]:
    scope_count = 0
    findings: list[Finding] = []
    for file_path in files:
        lines = read_lines(file_path)
        sections = find_comment_sections(lines)
        scopes = [("active", active_lines(lines, sections))]
        scopes.extend((f"comment-{index}", comment_lines(lines, section)) for index, section in enumerate(sections, start=1))
        for scope, scope_lines in scopes:
            scope_count += 1
            findings.extend(audit_list_scope(file_path, scope, scope_lines, review_unpunctuated))
    return scope_count, findings


def find_closing_delimiter(line: str, index: int, delimiter: str) -> int:
    cursor = index
    while cursor <= len(line) - len(delimiter):
        if line[cursor] == "\\":
            cursor += 2
            continue
        if line.startswith(delimiter, cursor):
            return cursor
        cursor += 1
    return -1


def transform_inline_emphasis(segment: str) -> str:
    boundary_before = r"(^|[\s([{'\">:;,!?-])"
    boundary_after = r"(?=$|[\s).,;:!?\]}'\"<-])"
    content = r"([^\s*](?:[^*\n]*?[^\s*])?)"
    result = segment
    for count, replacement in ((3, "___"), (2, "__"), (1, "_")):
        pattern = re.compile(f"{boundary_before}\\*{{{count}}}{content}\\*{{{count}}}{boundary_after}")
        result = pattern.sub(rf"\1{replacement}\2{replacement}", result)
    return result


def transform_emphasis(line: str) -> str:
    masked: list[str] = []
    protected_spans: list[str] = []
    index = 0
    while index < len(line):
        character = line[index]
        if character == "`":
            delimiter_match = re.match(r"`+", line[index:])
            if delimiter_match:
                delimiter = delimiter_match.group(0)
                close_at = find_closing_delimiter(line, index + len(delimiter), delimiter)
                if close_at >= 0:
                    token = f"\x00{len(protected_spans)}\x00"
                    protected_spans.append(line[index : close_at + len(delimiter)])
                    masked.append(token)
                    index = close_at + len(delimiter)
                    continue
        if character == "$" and (index == 0 or line[index - 1] != "\\"):
            delimiter = "$$" if line.startswith("$$", index) else "$"
            close_at = find_closing_delimiter(line, index + len(delimiter), delimiter)
            if close_at >= 0:
                token = f"\x00{len(protected_spans)}\x00"
                protected_spans.append(line[index : close_at + len(delimiter)])
                masked.append(token)
                index = close_at + len(delimiter)
                continue
        masked.append(character)
        index += 1

    transformed = transform_inline_emphasis("".join(masked))
    return re.sub(r"\x00(\d+)\x00", lambda match: protected_spans[int(match.group(1))], transformed)


def transform_list_markers(line: str) -> str:
    transformed = re.sub(r"^(\s*)\*\s+(?=\S)", r"\1- ", line)
    return re.sub(r"^(\s*-\s+)\*\s+(?=\S)", r"\1- ", transformed)


def audit_marker_policy(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for file_path in files:
        lines = read_lines(file_path)
        fences: list[Fence] = []
        in_front_matter = bool(lines and lines[0].strip() == "---")
        in_math_block = False
        for index, line in enumerate(lines, start=1):
            if in_front_matter:
                if index > 1 and line.strip() in {"---", "..."}:
                    in_front_matter = False
                continue

            fence = parse_fence(line)
            if fence:
                if closes_fence(fence, fences):
                    fences.pop()
                    continue
                fences.append(fence)
                transformed_marker = transform_list_markers(line)
                if transformed_marker != line:
                    findings.append(Finding(file_path, "raw", index, "ASTERISK_LIST_MARKER", line.strip()))
                continue

            if line.lstrip().startswith("$$"):
                in_math_block = not in_math_block
                continue
            if in_math_block or any(open_fence.is_literal for open_fence in fences):
                continue

            transformed_marker = transform_list_markers(line)
            transformed_emphasis = transform_emphasis(transformed_marker)
            if transformed_marker != line:
                findings.append(Finding(file_path, "raw", index, "ASTERISK_LIST_MARKER", line.strip()))
            if transformed_emphasis != transformed_marker:
                findings.append(Finding(file_path, "raw", index, "ASTERISK_EMPHASIS", line.strip()))
    return findings


def print_findings(title: str, findings: list[Finding]) -> None:
    if not findings:
        print(f"{title}: clean")
        return
    print(f"{title}: {len(findings)} issue(s)")
    for finding in findings:
        print(f"{display_path(finding.file_path)}:{finding.line} [{finding.scope}] {finding.category}: {finding.detail}")


def run_build() -> bool:
    print("Running dts docs build...")
    return subprocess.run(("dts", "docs", "build"), cwd=ROOT, check=False).returncode == 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Duckietown Manual Markdown, MyST, and commented content.")
    parser.add_argument("--file", action="append", type=Path, default=[], help="Audit one Markdown file; may be repeated.")
    parser.add_argument("--build", action="store_true", help="Build the Manual after audit checks pass.")
    parser.add_argument(
        "--review-unpunctuated",
        action="store_true",
        help="Also report non-structured list items without terminal punctuation for editorial review.",
    )
    arguments = parser.parse_args()

    try:
        files = markdown_files(arguments.file)
    except ValueError as error:
        parser.error(str(error))

    succeeded = run_markdownlint(files)

    include_findings = check_include_targets(files)
    print_findings("MyST include targets", include_findings)
    succeeded = succeeded and not include_findings

    comment_count, comment_findings = markdownlint_comments(files)
    print_findings(f"Comment Markdownlint ({comment_count} section(s))", comment_findings)
    succeeded = succeeded and not comment_findings

    marker_findings = audit_marker_policy(files)
    print_findings("Markdown marker policy", marker_findings)
    succeeded = succeeded and not marker_findings

    scope_count, list_findings = audit_lists_and_fences(files, arguments.review_unpunctuated)
    print_findings(f"MyST list and fence policy ({scope_count} scope(s))", list_findings)
    succeeded = succeeded and not list_findings

    if arguments.build and succeeded:
        succeeded = run_build()

    return 0 if succeeded else 1


if __name__ == "__main__":
    raise SystemExit(main())
