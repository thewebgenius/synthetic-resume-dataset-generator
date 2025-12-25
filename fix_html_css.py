"""
Fix HTML files by inlining CSS to work with wkhtmltopdf
"""
from pathlib import Path
import re

HTML_DIR = Path("output/html")
TEMPLATES_DIR = Path("templates")

def fix_html_files():
    """Inline CSS in all HTML files to fix PDF conversion issues"""
    html_files = list(HTML_DIR.glob("*.html"))
    
    print(f"Fixing {len(html_files)} HTML files...")
    fixed = 0
    
    for html_file in html_files:
        # Extract template ID from filename
        match = re.search(r'_t(\d{2})\.html', html_file.name)
        template_id = match.group(1) if match else "01"
        
        # Read HTML
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Only fix if not already fixed
        if '<link rel="stylesheet" href="style.css">' in html_content:
            # Load CSS
            css_path = TEMPLATES_DIR / f"template_{template_id}" / "style.css"
            
            if css_path.exists():
                with open(css_path, "r", encoding="utf-8") as f:
                    css_content = f.read()
                
                # Replace link with inline style
                html_content = html_content.replace(
                    '<link rel="stylesheet" href="style.css">',
                    f'<style>\n{css_content}\n    </style>'
                )
                
                # Write back
                with open(html_file, "w", encoding="utf-8") as f:
                    f.write(html_content)
                
                fixed += 1
                if fixed % 100 == 0:
                    print(f"  Fixed {fixed} files...")
    
    print(f"✓ Fixed {fixed} HTML files with inline CSS")

if __name__ == "__main__":
    fix_html_files()
