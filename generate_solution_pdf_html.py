"""
generate_solution_pdf_html.py - Converts solution_doc.md into a print-ready HTML page
Optimized for 2-Page A4 PDF export via Chrome/Edge (Ctrl+P -> Save as PDF).
"""

import os
import re

def markdown_to_html(md_text: str) -> str:
    # Code blocks (ASCII diagrams, etc.)
    def replace_code_block(match):
        code_content = match.group(1).replace("<", "&lt;").replace(">", "&gt;")
        return f"<pre style='background:#f4f6f8; border:1px solid #d1d5db; padding:8px 12px; border-radius:6px; font-family:Consolas, monospace; font-size:8.5pt; line-height:1.2; overflow-x:auto;'>{code_content}</pre>"
    
    html = re.sub(r"```(?:[a-zA-Z0-9_-]+)?\s*([\s\S]*?)\s*```", replace_code_block, md_text)
    # Inline code
    html = re.sub(r"`([^`]+)`", r"<code>\1</code>", html)
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
    # Horizontal rules
    html = re.sub(r"^---$", r"<hr style='border:none; border-top:1px solid #e0e0e0; margin:10px 0;'/>", html, flags=re.MULTILINE)
    
    # Clean Paragraph separation
    parts = html.split("\n\n")
    processed_parts = []
    for part in parts:
        p_strip = part.strip()
        if not p_strip:
            continue
        if p_strip.startswith("<h") or p_strip.startswith("<pre") or p_strip.startswith("<hr") or p_strip.startswith("<li>"):
            processed_parts.append(p_strip)
        else:
            processed_parts.append(f"<p>{p_strip}</p>")
    return "\n".join(processed_parts)

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

