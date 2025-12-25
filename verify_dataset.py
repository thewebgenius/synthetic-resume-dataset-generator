"""
Dataset verification and statistics script.
Checks all generated files and reports distribution across templates.
"""

from pathlib import Path
import json
import re
from collections import Counter

def extract_template_id(filename):
    """Extract template ID from filename."""
    match = re.search(r'_t(\d{2})', filename)
    return match.group(1) if match else None

def verify_dataset():
    print("\n" + "="*70)
    print(" DATASET VERIFICATION & STATISTICS")
    print("="*70)
    
    # Check JSON resumes
    json_dir = Path("data/resumes")
    json_files = list(json_dir.glob("*.json"))
    print(f"\n✓ JSON Resumes: {len(json_files)} files")
    
    # Check HTML files
    html_dir = Path("output/html")
    html_files = list(html_dir.glob("*.html"))
    print(f"✓ HTML Files: {len(html_files)} files")
    
    # Analyze template distribution in HTML files
    if html_files:
        html_templates = [extract_template_id(f.name) for f in html_files]
        html_templates = [t for t in html_templates if t]  # Filter None
        template_counts = Counter(html_templates)
        
        print("\n  Template Distribution (HTML):")
        for template_id in sorted(template_counts.keys()):
            count = template_counts[template_id]
            bar = "█" * (count // 5)  # Visual bar chart
            print(f"    Template {template_id}: {count:4d} {bar}")
    
    # Check PDF files
    pdf_dir = Path("output/pdf")
    pdf_files = list(pdf_dir.glob("*.pdf"))
    print(f"\n✓ PDF Files: {len(pdf_files)} files")
    
    # Check images
    clean_dir = Path("output/images/clean")
    noisy_dir = Path("output/images/noisy")
    clean_images = list(clean_dir.glob("*.png"))
    noisy_images = list(noisy_dir.glob("*.png"))
    
    print(f"✓ Clean Images: {len(clean_images)} files")
    print(f"✓ Noisy Images: {len(noisy_images)} files")
    
    # Check annotations
    annot_dir = Path("annotations")
    annot_files = list(annot_dir.glob("*.txt"))
    print(f"✓ Annotation Files: {len(annot_files)} files")
    
    # Verify annotation format
    if annot_files:
        sample_annot = annot_files[0]
        with open(sample_annot) as f:
            lines = f.readlines()
        print(f"\n  Sample annotation ({sample_annot.name}):")
        print(f"    Lines: {len(lines)} (expected: 6 sections)")
        if lines:
            print(f"    Format: {lines[0].strip()}")
    
    # Check templates
    templates_dir = Path("templates")
    templates = [d for d in templates_dir.iterdir() if d.is_dir()]
    print(f"\n✓ Templates: {len(templates)} folders")
    
    for template in sorted(templates):
        has_html = (template / "resume.html").exists()
        has_css = (template / "style.css").exists()
        has_config = (template / "layout_config.json").exists()
        
        status = "✓" if (has_html and has_css and has_config) else "✗"
        print(f"  {status} {template.name}: HTML={has_html} CSS={has_css} Config={has_config}")
    
    # Overall summary
    print("\n" + "="*70)
    print(" SUMMARY")
    print("="*70)
    
    expected = 1000
    issues = []
    
    if len(json_files) != expected:
        issues.append(f"JSON files: {len(json_files)} (expected {expected})")
    if len(html_files) != expected:
        issues.append(f"HTML files: {len(html_files)} (expected {expected})")
    if len(pdf_files) != expected:
        issues.append(f"PDF files: {len(pdf_files)} (expected {expected})")
    if len(clean_images) != expected:
        issues.append(f"Clean images: {len(clean_images)} (expected {expected})")
    if len(noisy_images) != expected:
        issues.append(f"Noisy images: {len(noisy_images)} (expected {expected})")
    if len(annot_files) != expected:
        issues.append(f"Annotations: {len(annot_files)} (expected {expected})")
    
    if not issues:
        print("\n✅ All checks passed! Dataset is complete.")
        print(f"   Total resumes: {expected}")
        print(f"   Total images: {len(clean_images) + len(noisy_images)}")
        print(f"   Templates used: {len(template_counts)}")
    else:
        print("\n⚠️  Issues found:")
        for issue in issues:
            print(f"   - {issue}")
    
    # File size estimation
    if pdf_files:
        total_size = sum(f.stat().st_size for f in pdf_files[:10])  # Sample 10 files
        avg_size = total_size / 10
        estimated_total = (avg_size * len(pdf_files)) / (1024**2)  # MB
        print(f"\n💾 Estimated PDF storage: {estimated_total:.1f} MB")
    
    if clean_images:
        total_size = sum(f.stat().st_size for f in clean_images[:10])
        avg_size = total_size / 10
        estimated_total = (avg_size * (len(clean_images) + len(noisy_images))) / (1024**2)
        print(f"💾 Estimated Image storage: {estimated_total:.1f} MB")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    verify_dataset()
