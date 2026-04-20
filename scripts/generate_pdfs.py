from pathlib import Path
import re

from fpdf import FPDF

ROOT = Path(__file__).resolve().parents[1]

SOURCES = [
    ("pitchdeck/slides.md", "pitchdeck/slides.pdf", "Clisonix Pitch Deck"),
    ("docs/what-is-clisonix.md", "docs/what-is-clisonix.pdf", "What is Clisonix"),
    ("docs/1-pager.md", "docs/1-pager.pdf", "Clisonix 1-Pager"),
    ("docs/executive-summary.md", "docs/executive-summary.pdf", "Executive Summary"),
    ("docs/due-diligence.md", "docs/due-diligence.pdf", "Due Diligence"),
    ("docs/term-sheet.md", "docs/term-sheet.pdf", "Term Sheet"),
    ("funding/vc-list.md", "funding/vc-list.pdf", "VC Target List"),
    ("funding/foerderantrag.md", "funding/foerderantrag.pdf", "Funding Application Notes"),
    ("scripts/teaser-video.md", "scripts/teaser-video.pdf", "Teaser Video Script"),
]


def sanitize_text(text: str) -> str:
    replacements = {
        "\u20ac": "EUR ",
        "\u2013": "-",
        "\u2014": "-",
        "\u2192": "->",
        "\u2194": "<->",
        "\u2713": "[OK]",
        "\u2610": "[ ]",
        "\u2717": "[X]",
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove most emoji/symbol ranges that commonly break PDF rendering.
    text = re.sub(r"[\U0001F300-\U0001FAFF]", "", text)
    text = re.sub(r"[\u2600-\u27BF]", "", text)

    # Keep output ASCII-only for maximal cross-platform PDF safety.
    text = text.encode("ascii", "ignore").decode("ascii")
    return text.strip()


def write_line(pdf: FPDF, text: str, level: str = "normal") -> None:
    clean = sanitize_text(text)
    if not clean:
        pdf.ln(3)
        return

    if level == "h1":
        pdf.set_font("ArialUnicode", "B", 18)
        pdf.multi_cell(0, 10, clean, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1)
    elif level == "h2":
        pdf.set_font("ArialUnicode", "B", 14)
        pdf.multi_cell(0, 8, clean, new_x="LMARGIN", new_y="NEXT")
    elif level == "h3":
        pdf.set_font("ArialUnicode", "B", 12)
        pdf.multi_cell(0, 7, clean, new_x="LMARGIN", new_y="NEXT")
    elif level == "bullet":
        pdf.set_font("ArialUnicode", "", 11)
        pdf.multi_cell(0, 6, f"- {clean}", new_x="LMARGIN", new_y="NEXT")
    elif level == "table":
        pdf.set_font("ArialUnicode", "", 10)
        row = " | ".join([p.strip() for p in clean.strip("|").split("|") if p.strip()])
        if row:
            pdf.multi_cell(0, 5.5, row, new_x="LMARGIN", new_y="NEXT")
    else:
        pdf.set_font("ArialUnicode", "", 11)
        pdf.multi_cell(0, 6.5, clean, new_x="LMARGIN", new_y="NEXT")


def markdown_to_pdf(src: Path, dst: Path, doc_title: str) -> None:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=14)
    pdf.add_page()

    font_path = Path("C:/Windows/Fonts/arial.ttf")
    pdf.add_font("ArialUnicode", "", str(font_path))
    pdf.add_font("ArialUnicode", "B", str(font_path))

    write_line(pdf, doc_title, "h1")

    text = src.read_text(encoding="utf-8")
    lines = text.splitlines()

    for line in lines:
        stripped = line.rstrip()

        if stripped.startswith("# "):
            write_line(pdf, stripped[2:], "h1")
            continue
        if stripped.startswith("## "):
            write_line(pdf, stripped[3:], "h2")
            continue
        if stripped.startswith("### "):
            write_line(pdf, stripped[4:], "h3")
            continue
        if stripped.startswith("- ") or stripped.startswith("* "):
            write_line(pdf, stripped[2:], "bullet")
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            if set(stripped.replace("|", "").strip()) == {"-"}:
                continue
            write_line(pdf, stripped, "table")
            continue

        clean = stripped.replace("**", "").replace("__", "")
        write_line(pdf, clean)

    dst.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(dst))


def main() -> None:
    for src_rel, dst_rel, title in SOURCES:
        src = ROOT / src_rel
        dst = ROOT / dst_rel
        markdown_to_pdf(src, dst, title)
        print(f"Generated: {dst_rel}")


if __name__ == "__main__":
    main()
