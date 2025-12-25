# Resume Generator - Scaled Pipeline

## Overview
This system generates 1000 synthetic resumes across 10 visually distinct templates for computer vision research. Each resume goes through a complete pipeline: JSON → HTML → PDF → Image → Annotation.

## Project Structure

```
resume_generator/
├── data/
│   └── resumes/                    # 1000 JSON resume files
├── templates/
│   ├── template_01/                # Vertical single-column (original)
│   ├── template_02/                # Two-column, left sidebar
│   ├── template_03/                # Two-column, right sidebar
│   ├── template_04/                # Header-centric, large header
│   ├── template_05/                # Minimalist with whitespace
│   ├── template_06/                # Dense compact layout
│   ├── template_07/                # Skills-first layout
│   ├── template_08/                # Projects-first layout
│   ├── template_09/                # Three-section layout
│   └── template_10/                # Modern split layout
│       ├── resume.html
│       ├── style.css
│       └── layout_config.json      # YOLO annotation coordinates
├── output/
│   ├── html/                       # 1000 HTML files (resume_XXXX_tYY.html)
│   ├── pdf/                        # 1000 PDF files (resume_XXXX_tYY.pdf)
│   └── images/
│       ├── clean/                  # 1000 clean images
│       └── noisy/                  # 1000 noisy augmented images
└── annotations/                    # 1000 YOLO-format annotation files
```

## Template Designs

| Template | Layout Type | Visual Characteristics |
|----------|-------------|------------------------|
| 01 | Vertical single-column | Classic Arial font, simple borders |
| 02 | Two-column left sidebar | Education/skills in gray sidebar |
| 03 | Two-column right sidebar | Georgia serif font, red accents |
| 04 | Header-centric | Large dark header (20% height) |
| 05 | Minimalist | Lots of whitespace, sparse sections |
| 06 | Dense | Compact spacing, small fonts |
| 07 | Skills-first | Skills prominently at top with green theme |
| 08 | Projects-first | Dark theme with monospace font |
| 09 | Three-section | Golden accents, three-column layout |
| 10 | Modern gradient | Purple gradient header, split layout |

## Pipeline Execution

### Step 1: Generate 1000 JSON Resumes
```bash
python generate_resumes.py
```
- Creates 1000 unique resume JSON files
- Random seed = 42 (reproducible)
- Output: `data/resumes/*.json`

### Step 2: Render HTML with Random Templates
```bash
python batch_render.py
```
- Randomly assigns one of 10 templates to each resume
- Random seed = 100 (reproducible template assignment)
- Output: `output/html/resume_XXXX_tYY.html`
  - `XXXX` = resume number (0001-1000)
  - `YY` = template ID (01-10)

### Step 3: Convert HTML → PDF
```bash
python html_to_pdf.py
```
- Converts all HTML files to PDF
- Requires wkhtmltopdf
- Output: `output/pdf/resume_XXXX_tYY.pdf`

### Step 4: Convert PDF → Images
```bash
python pdf_to_image.py
```
- Converts PDFs to 300 DPI PNG images
- Requires poppler (pdftoppm)
- Output: `output/images/resume_XXXX_tYY-1.png`

### Step 5: Separate Clean & Noisy Images
```bash
# Move clean images
Move-Item output/images/*.png output/images/clean/

# Create noisy augmented versions
python add_noise.py
```
- Applies rotation, blur, noise, contrast variations
- Output: `output/images/noisy/*.png`

### Step 6: Generate Template-Aware Annotations
```bash
python create_annotations.py
```
- Reads `layout_config.json` for each template
- Generates YOLO-format bounding boxes
- Automatically detects template ID from filename
- Output: `annotations/resume_XXXX_tYY-1.txt`

## YOLO Annotation Format

Each annotation file contains 6 lines (one per section):
```
<class_id> <x_center> <y_center> <width> <height>
```

**Class Mapping:**
- 0: Header
- 1: Education
- 2: Skills
- 3: Projects
- 4: Experience
- 5: Hobbies

All coordinates are normalized (0.0 to 1.0).

## Layout Configuration System

Each template has a `layout_config.json` defining section positions:

```json
{
  "template_id": "02",
  "layout_type": "two_column_left_sidebar",
  "sections": {
    "header": {
      "x_start": 0.0,
      "x_end": 1.0,
      "y_start": 0.00,
      "y_end": 0.15
    },
    "education": {
      "x_start": 0.0,
      "x_end": 0.35,
      "y_start": 0.15,
      "y_end": 0.40
    }
  }
}
```

## Reproducibility

- **JSON Generation:** `random.seed(42)` in `generate_resumes.py`
- **Template Assignment:** `random.seed(100)` in `batch_render.py`
- Same seeds → identical dataset every time

## Dataset Statistics

- **Total resumes:** 1000
- **Templates per resume:** 1 (randomly assigned)
- **Expected distribution:** ~100 resumes per template
- **Images:** 1000 clean + 1000 noisy = 2000 total
- **Annotations:** 1000 files (6 bounding boxes each)

## File Naming Convention

| Stage | Pattern | Example |
|-------|---------|---------|
| JSON | `{uuid}.json` | `05baedb6-d4f6-49a3-9220-65fb1456e042.json` |
| HTML | `resume_{id:04d}_t{template:02d}.html` | `resume_0042_t07.html` |
| PDF | `resume_{id:04d}_t{template:02d}.pdf` | `resume_0042_t07.pdf` |
| Image | `resume_{id:04d}_t{template:02d}-1.png` | `resume_0042_t07-1.png` |
| Annotation | `resume_{id:04d}_t{template:02d}-1.txt` | `resume_0042_t07-1.txt` |

## Dependencies

- Python 3.x
- Pillow (image processing)
- NumPy (noise generation)
- wkhtmltopdf (HTML → PDF)
- poppler (PDF → Image)

## Usage for CNN Training

1. **Data Split:** Divide clean/noisy images into train/val/test sets
2. **Input:** Noisy images from `output/images/noisy/`
3. **Target:** Clean images from `output/images/clean/`
4. **Metadata:** Template ID available in filename for stratified sampling

## Notes

- Template assignment is random (not sequential) for better training diversity
- Layout configs enable template-specific bounding boxes
- All paths use forward slashes `/` for cross-platform compatibility
- Original `template_1` folder can be deleted (now `template_01`)

## Future Enhancements

- Add more template variations (color schemes, fonts)
- Implement sequential assignment (100 per template) for controlled experiments
- Generate template-specific augmentations
- Create train/val/test split script with stratification
