from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
)
from reportlab.lib.units import inch
import re


INPUT_FILE = "news_blog_post.md"
OUTPUT_FILE = "news_blog_post.pdf"


# Read Markdown
with open(INPUT_FILE, "r", encoding="utf-8") as file:
    content = file.read()


# PDF document
doc = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=A4,
    rightMargin=50,
    leftMargin=50,
    topMargin=50,
    bottomMargin=50,
)


styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "Title",
    parent=styles["Title"],
    fontSize=24,
    leading=30,
    alignment=TA_CENTER,
    spaceAfter=20,
)

heading_style = ParagraphStyle(
    "Heading",
    parent=styles["Heading2"],
    fontSize=17,
    leading=22,
    spaceBefore=15,
    spaceAfter=8,
)

body_style = ParagraphStyle(
    "Body",
    parent=styles["BodyText"],
    fontSize=11,
    leading=17,
    spaceAfter=10,
)


story = []


for line in content.splitlines():

    line = line.strip()

    if not line:
        story.append(Spacer(1, 8))
        continue

    # H1
    if line.startswith("# "):
        text = line[2:].strip()
        story.append(Paragraph(text, title_style))

    # H2
    elif line.startswith("## "):
        text = line[3:].strip()
        story.append(Paragraph(text, heading_style))

    # H3
    elif line.startswith("### "):
        text = line[4:].strip()
        story.append(Paragraph(text, heading_style))

    # Bullet points
    elif line.startswith("- "):
        text = line[2:].strip()
        story.append(
            Paragraph(
                f"• {text}",
                body_style
            )
        )

    # Numbered list
    elif re.match(r"^\d+\.\s", line):
        text = re.sub(r"^\d+\.\s", "", line)
        story.append(
            Paragraph(
                f"• {text}",
                body_style
            )
        )

    # Normal paragraph
    else:
        story.append(
            Paragraph(
                line,
                body_style
            )
        )


doc.build(story)

print(f"PDF created successfully: {OUTPUT_FILE}")
