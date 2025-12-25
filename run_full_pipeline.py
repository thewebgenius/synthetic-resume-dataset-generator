"""
Master pipeline script to run all stages of resume generation.
Executes: JSON → HTML → PDF → Image → Clean/Noisy → Annotations
"""

import subprocess
import sys
from pathlib import Path
import time

def run_step(step_name, script_name, description):
    """Run a pipeline step and report results."""
    print("\n" + "="*70)
    print(f"STEP: {step_name}")
    print(f"Description: {description}")
    print("="*70)
    
    start_time = time.time()
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        elapsed = time.time() - start_time
        print(f"✓ {step_name} completed in {elapsed:.2f} seconds")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {step_name} FAILED!")
        print(e.stderr)
        return False

def move_images_to_clean():
    """Move generated images to clean folder."""
    print("\n" + "="*70)
    print("STEP: Move Images to Clean Folder")
    print("="*70)
    
    images_dir = Path("output/images")
    clean_dir = images_dir / "clean"
    
    # Get all PNG files in the root images directory
    png_files = list(images_dir.glob("*.png"))
    
    if not png_files:
        print("No images found to move.")
        return True
    
    moved = 0
    for img_file in png_files:
        try:
            img_file.rename(clean_dir / img_file.name)
            moved += 1
        except Exception as e:
            print(f"Error moving {img_file.name}: {e}")
    
    print(f"✓ Moved {moved} images to clean/ folder")
    return True

def main():
    print("\n" + "🚀 "*20)
    print(" RESUME GENERATION PIPELINE - FULL EXECUTION")
    print("🚀 "*20)
    print("\nThis will generate 1000 resumes with 10 different templates")
    print("Total stages: 6")
    print("\n⚠️  This may take several minutes to complete...")
    
    input("\nPress ENTER to start the pipeline...")
    
    overall_start = time.time()
    
    # Stage 1: Generate JSON resumes
    if not run_step(
        "1/6 - Generate JSON Resumes",
        "generate_resumes.py",
        "Creating 1000 unique resume JSON files"
    ):
        return
    
    # Stage 2: Render HTML with templates
    if not run_step(
        "2/6 - Render HTML",
        "batch_render.py",
        "Converting JSON to HTML using 10 random templates"
    ):
        return
    
    # Stage 3: Convert HTML to PDF
    if not run_step(
        "3/6 - HTML → PDF",
        "html_to_pdf.py",
        "Converting HTML files to PDF format"
    ):
        return
    
    # Stage 4: Convert PDF to Images
    if not run_step(
        "4/6 - PDF → Images",
        "pdf_to_image.py",
        "Converting PDFs to 300 DPI PNG images"
    ):
        return
    
    # Stage 5: Move images and create noisy versions
    if not move_images_to_clean():
        return
    
    if not run_step(
        "5/6 - Generate Noisy Images",
        "add_noise.py",
        "Creating augmented noisy versions of clean images"
    ):
        return
    
    # Stage 6: Create annotations
    if not run_step(
        "6/6 - Create Annotations",
        "create_annotations.py",
        "Generating YOLO-format annotations for all templates"
    ):
        return
    
    # Summary
    total_time = time.time() - overall_start
    
    print("\n" + "✅ "*20)
    print(" PIPELINE COMPLETED SUCCESSFULLY!")
    print("✅ "*20)
    print(f"\nTotal execution time: {total_time/60:.2f} minutes")
    print("\nGenerated files:")
    print("  - 1000 JSON resumes in data/resumes/")
    print("  - 1000 HTML files in output/html/")
    print("  - 1000 PDF files in output/pdf/")
    print("  - 1000 clean images in output/images/clean/")
    print("  - 1000 noisy images in output/images/noisy/")
    print("  - 1000 annotation files in annotations/")
    print("\nDataset is ready for CNN training!")
    print("\nSee README_SCALING.md for detailed documentation.")

if __name__ == "__main__":
    main()
