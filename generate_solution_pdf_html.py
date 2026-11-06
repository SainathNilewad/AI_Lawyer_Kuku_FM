"""
generate_solution_pdf_html.py - Converts solution_doc.md into a print-ready HTML page
Optimized for 2-Page A4 PDF export via Chrome/Edge (Ctrl+P -> Save as PDF).
"""

import os
import re

def markdown_to_html(md_text: str) -> str:
    # Basic markdown parsing
    html = md_text
    # Headers
    html = re.sub(r"^### (.*)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
    html = re.sub(r"^## (.*)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^# (.*)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)
    # Bold & Italic
    html = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.*?)\*", r"<em>\1</em>", html)
    # Lists
    html = re.sub(r"^\* (.*)$", r"<li>\1</li>", html, flags=re.MULTILINE)
    html = re.sub(r"^- (.*)$", r"<li>\1</li>", html, flags=re.MULTILINE)
    # Paragraphs / Newlines
    html = html.replace("\n\n", "</p><p>")
    html = f"<p>{html}</p>"
    return html

def build_print_ready_html():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(base_dir, "solution_doc.md")
    
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
        
    html_body = markdown_to_html(md_content)

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>NyayaMitra - AI Legal Generalist Solution Document</title>
    <style>
        @page {{
            size: A4;
            margin: 15mm 15mm 15mm 15mm;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            color: #212121;
            line-height: 1.45;
            font-size: 10.5pt;
            margin: 0;
            padding: 10px;
        }}
        h1 {{
            color: #1a237e;
            font-size: 17pt;
            margin-bottom: 2px;
            border-bottom: 2px solid #1a237e;
            padding-bottom: 4px;
        }}
        h2 {{
            color: #0d47a1;
            font-size: 12.5pt;
            margin-top: 10px;
            margin-bottom: 4px;
            border-bottom: 1px solid #e0e0e0;
            padding-bottom: 2px;
        }}
        h3 {{
            color: #263238;
            font-size: 11pt;
            margin-top: 8px;
            margin-bottom: 3px;
        }}
        p {{
            margin-top: 4px;
            margin-bottom: 6px;
        }}
        ul, ol {{
            margin-top: 4px;
            margin-bottom: 6px;
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 2px;
        }}
        strong {{
            color: #1a237e;
        }}
        code {{
            background: #f1f3f4;
            padding: 1px 4px;
            border-radius: 3px;
            font-size: 9.5pt;
        }}
        .print-btn {{
            position: fixed;
            top: 15px;
            right: 15px;
            background: #1a237e;
            color: white;
            border: none;
            padding: 10px 18px;
            border-radius: 6px;
            cursor: pointer;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }}
        @media print {{
            .print-btn {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <button class="print-btn" onclick="window.print()">🖨️ Print / Save as PDF</button>
    {html_body}
</body>
</html>
"""
    out_path = os.path.join(base_dir, "solution_doc.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated print-ready HTML at: {out_path}")

if __name__ == "__main__":
    build_print_ready_html()
