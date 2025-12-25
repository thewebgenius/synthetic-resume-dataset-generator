import subprocess
from pathlib import Path
import re

HTML_DIR = Path("output/html")
PDF_DIR = Path("output/pdf")
TEMPLATES_DIR = Path("templates")

WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

def inline_css_in_html(html_content, template_id):
    """Inline the CSS directly into HTML to avoid path issues"""
    css_path = TEMPLATES_DIR / f"template_{template_id}" / "style.css"
    
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()
        
        # Replace link tag with inline style
        html_content = re.sub(
            r'<link rel="stylesheet" href="style\.css">',
            f'<style>{css_content}</style>',
            html_content
        )
    
    return html_content

def convert_html_to_pdf():
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    html_files = list(HTML_DIR.glob("*.html"))

    if not html_files:
        print("No HTML files found.")
        return
    
    success_count = 0
    fail_count = 0

    for html_file in html_files:
        # Extract template ID from filename
        match = re.search(r'_t(\d{2})\.html', html_file.name)
        template_id = match.group(1) if match else "01"
        
        # Read HTML and inline CSS
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        html_content = inline_css_in_html(html_content, template_id)
        
        # Write to temporary file
        temp_html = html_file.with_suffix(".tmp.html")
        with open(temp_html, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        pdf_file = PDF_DIR / html_file.with_suffix(".pdf").name

        command = [
            WKHTMLTOPDF_PATH,
            "--quiet",
            "--enable-local-file-access",
            str(temp_html.resolve()),
            str(pdf_file.resolve())
        ]

        try:
            subprocess.run(command, check=True, capture_output=True)
            success_count += 1
            if success_count % 100 == 0:
                print(f"✓ Converted {success_count} PDFs...")
        except Exception as e:
            fail_count += 1
        finally:
            # Clean up temp file
            if temp_html.exists():
                temp_html.unlink()
    
    print(f"\n✓ PDF Conversion Complete!")
    print(f"  Success: {success_count}")
    print(f"  Failed: {fail_count}")

if __name__ == "__main__":
    convert_html_to_pdf()
