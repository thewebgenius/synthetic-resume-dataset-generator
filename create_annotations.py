from PIL import Image
from pathlib import Path
import json
import re

IMAGE_DIR = Path("output/images/clean")
ANNOT_DIR = Path("annotations")
TEMPLATES_DIR = Path("templates")
ANNOT_DIR.mkdir(parents=True, exist_ok=True)

# YOLO class mapping:
# 0 header, 1 education, 2 skills, 3 projects, 4 experience, 5 hobbies

CLASS_MAP = {
    "header": 0,
    "education": 1,
    "skills": 2,
    "projects": 3,
    "experience": 4,
    "hobbies": 5
}

def extract_template_id(filename):
    """Extract template ID from filename like 'resume_0042_t07-1.png' -> '07'"""
    match = re.search(r'_t(\d{2})', filename)
    if match:
        return match.group(1)
    return "01"  # Default to template 01 if not found

def create_annotations():
    image_files = list(IMAGE_DIR.glob("*.png"))

    if not image_files:
        print("No images found in clean folder.")
        return

    for img_path in image_files:
        # Extract template ID from filename
        template_id = extract_template_id(img_path.name)
        
        # Load layout configuration for this template
        config_path = TEMPLATES_DIR / f"template_{template_id}" / "layout_config.json"
        
        if not config_path.exists():
            print(f"⚠️  Config not found for template {template_id}, skipping {img_path.name}")
            continue
            
        with open(config_path, "r") as f:
            layout = json.load(f)
        
        # Get image dimensions
        img = Image.open(img_path)
        w, h = img.size

        lines = []
        
        # Generate YOLO format annotations based on layout config
        for section_name, bounds in layout["sections"].items():
            if section_name not in CLASS_MAP:
                continue
                
            class_id = CLASS_MAP[section_name]
            
            # Extract bounds (support both full and simple formats)
            x_start = bounds.get("x_start", 0.0)
            x_end = bounds.get("x_end", 1.0)
            y_start = bounds.get("y_start", bounds.get("y0", 0.0))  # Fallback to y0/y1
            y_end = bounds.get("y_end", bounds.get("y1", 1.0))
            
            # Calculate YOLO format: class x_center y_center width height (all normalized)
            x_center = (x_start + x_end) / 2
            y_center = (y_start + y_end) / 2
            box_w = x_end - x_start
            box_h = y_end - y_start

            lines.append(
                f"{class_id} {x_center:.6f} {y_center:.6f} {box_w:.6f} {box_h:.6f}"
            )

            lines.append(
                f"{class_id} {x_center:.6f} {y_center:.6f} {box_w:.6f} {box_h:.6f}"
            )

        # Save annotation file
        label_path = ANNOT_DIR / f"{img_path.stem}.txt"
        with open(label_path, "w") as f:
            f.write("\n".join(lines))

        print(f"✓ {label_path.name} (Template {template_id})")

if __name__ == "__main__":
    create_annotations()
