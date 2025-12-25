# Quick Start Guide - Resume Generator

## 🚀 Run Full Pipeline (Easiest)

```bash
python run_full_pipeline.py
```

**What it does:**
- Generates 1000 JSON resumes
- Renders with 10 random templates
- Converts to PDF → Images
- Separates clean/noisy
- Creates annotations
- **Total time:** ~10-15 minutes

---

## 📊 Verify Dataset

```bash
python verify_dataset.py
```

**Output:**
- File counts for each stage
- Template distribution chart
- Format validation
- Storage estimates

---

## 🔧 Manual Control

### Generate specific number of resumes:
```python
# Edit generate_resumes.py
save_resumes(100)  # Change 1000 to desired number
```

### Test with specific template:
```python
# Edit batch_render.py
template_id = 5  # Force template 05
# Instead of: template_id = random.randint(1, 10)
```

### Sequential template assignment:
```python
# In batch_render.py, replace random assignment with:
template_id = ((idx - 1) // 100) + 1  # 100 per template
```

---

## 📁 Output Structure

```
data/resumes/           → 1000 JSON files
output/html/            → 1000 HTML (resume_XXXX_tYY.html)
output/pdf/             → 1000 PDF (resume_XXXX_tYY.pdf)
output/images/clean/    → 1000 clean PNG
output/images/noisy/    → 1000 noisy PNG
annotations/            → 1000 YOLO txt files
```

---

## 🎯 Template IDs

- `t01` - Classic vertical
- `t02` - Left sidebar (gray)
- `t03` - Right sidebar (red)
- `t04` - Large header (dark)
- `t05` - Minimalist (spacious)
- `t06` - Dense compact
- `t07` - Skills-first (green)
- `t08` - Projects-first (dark theme)
- `t09` - Three-column (gold)
- `t10` - Modern gradient (purple)

---

## 🔍 Filename Patterns

```
resume_0042_t07-1.png
       │    │   │
       │    │   └─ Page (always 1)
       │    └───── Template (01-10)
       └────────── Resume number (0001-1000)
```

---

## ⚙️ Dependencies

**Required:**
- Python 3.x
- Pillow: `pip install Pillow`
- NumPy: `pip install numpy`
- wkhtmltopdf: [Download](https://wkhtmltopdf.org/)
- poppler: [Download](https://github.com/oschwartz10612/poppler-windows/releases/)

**Update paths in scripts:**
- `html_to_pdf.py` → Line 7: wkhtmltopdf path
- `pdf_to_image.py` → Line 6: pdftoppm path

---

## 📝 YOLO Annotation Classes

```
0 = header
1 = education
2 = skills
3 = projects
4 = experience
5 = hobbies
```

**Format:** `class x_center y_center width height` (normalized 0-1)

---

## 🐛 Troubleshooting

### No HTML files generated
```bash
# Check if JSON files exist
ls data/resumes/

# Check template paths
ls templates/
```

### PDF conversion fails
```bash
# Verify wkhtmltopdf installed
wkhtmltopdf --version

# Update path in html_to_pdf.py
```

### Images not found
```bash
# Check PDF files exist
ls output/pdf/

# Verify poppler path in pdf_to_image.py
```

### Annotations incorrect
```bash
# Check layout_config.json exists for all templates
ls templates/template_*/layout_config.json
```

---

## 📚 Documentation Files

- `README_SCALING.md` - Complete system documentation
- `IMPLEMENTATION_SUMMARY.md` - What was changed/added
- `TEMPLATE_GUIDE.md` - Visual template comparison
- `QUICK_START.md` - This file

---

## 💡 Tips

**Faster testing:**
- Use 10-50 resumes instead of 1000
- Test one template at a time
- Check verify_dataset.py after each stage

**For CNN training:**
- Split: 70% train, 15% val, 15% test
- Input: noisy images
- Target: clean images
- Stratify by template ID for balanced distribution

**Storage optimization:**
- Keep only PNG images (delete PDF/HTML after generation)
- Compress annotations (they're tiny)
- Total ~600 MB for 1000 resumes

---

## ✅ Success Checklist

Run `verify_dataset.py` and confirm:
- [ ] 1000 JSON files
- [ ] 1000 HTML files
- [ ] 1000 PDF files
- [ ] 1000 clean images
- [ ] 1000 noisy images
- [ ] 1000 annotations
- [ ] 10 templates configured
- [ ] Template distribution ~100 each

---

**Ready to generate? Run:** `python run_full_pipeline.py`
