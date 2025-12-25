# Template Visual Comparison Guide

## Template 01 - Classic Vertical
**Layout:** Single column, vertical stacking
**Font:** Arial, sans-serif
**Style:** Clean, professional, traditional
**Colors:** Black text, simple borders
**Best for:** Standard corporate resumes

**Section Order (Top → Bottom):**
1. Header (0-12%)
2. Education (12-25%)
3. Skills (25-45%)
4. Projects (45-65%)
5. Experience (65-80%)
6. Hobbies (80-100%)

---

## Template 02 - Left Sidebar
**Layout:** Two-column with left sidebar
**Font:** Arial, sans-serif
**Style:** Modern, organized
**Colors:** Gray sidebar (#ecf0f1), blue accents (#2c3e50)
**Best for:** Highlighting education and skills

**Section Layout:**
- Header: Full width (0-15%)
- Left sidebar (0-35% width):
  - Education
  - Skills
  - Hobbies
- Right main (35-100% width):
  - Projects
  - Experience

---

## Template 03 - Right Sidebar
**Layout:** Two-column with right sidebar
**Font:** Georgia, serif
**Style:** Elegant, academic
**Colors:** Red accents (#e74c3c), pink sidebar (#fadbd8)
**Best for:** Projects and experience focus

**Section Layout:**
- Header: Full width (0-15%)
- Left main (0-65% width):
  - Projects
  - Experience
  - Education
- Right sidebar (65-100% width):
  - Skills
  - Hobbies

---

## Template 04 - Header-Centric
**Layout:** Large header + vertical sections
**Font:** Segoe UI, Tahoma
**Style:** Bold, eye-catching
**Colors:** Dark header (#34495e), white text
**Best for:** Strong personal branding

**Section Layout:**
- Header: Large 20% height with dark background
- Skills (20-38%)
- Education (38-53%)
- Projects (53-73%)
- Experience (73-90%)
- Hobbies (90-100%)

---

## Template 05 - Minimalist
**Layout:** Sparse vertical with whitespace
**Font:** Helvetica Neue
**Style:** Clean, minimal, spacious
**Colors:** Light grays, subtle text
**Best for:** Design-focused candidates

**Section Layout:**
- Large margins and spacing
- Header (0-18%)
- Education (20-35%)
- Skills (38-53%)
- Projects (56-73%)
- Experience (76-91%)
- Hobbies (93-100%)

---

## Template 06 - Dense Compact
**Layout:** Tight vertical stacking
**Font:** Verdana (small 12px)
**Style:** Information-dense, compact
**Colors:** Black, minimal decoration
**Best for:** Maximum information in minimal space

**Section Layout:**
- Small margins, tight line spacing
- Header (0-10%)
- Education (10-22%)
- Skills (22-42%)
- Projects (42-65%)
- Experience (65-85%)
- Hobbies (85-100%)

---

## Template 07 - Skills-First
**Layout:** Vertical with skills prominent
**Font:** Trebuchet MS
**Style:** Technical, professional
**Colors:** Green accents (#16a085), highlighted sections
**Best for:** Technical/engineering roles

**Section Order (Top → Bottom):**
1. Header (0-13%)
2. **Skills (13-35%)** ← Featured
3. Projects (35-58%)
4. Experience (58-75%)
5. Education (75-90%)
6. Hobbies (90-100%)

---

## Template 08 - Projects-First
**Layout:** Vertical with projects prominent
**Font:** Courier New (monospace)
**Style:** Tech/developer theme, dark
**Colors:** Dark background (#2d2d2d), blue/green accents
**Best for:** Developers, tech portfolios

**Section Order (Top → Bottom):**
1. Header (0-12%)
2. **Projects (12-40%)** ← Featured
3. Experience (40-60%)
4. Skills (60-78%)
5. Education (78-92%)
6. Hobbies (92-100%)

---

## Template 09 - Three-Section
**Layout:** Three-column layout
**Font:** Palatino Linotype (serif)
**Style:** Academic, traditional
**Colors:** Gold accents (#f39c12), warm tones
**Best for:** Academic/research positions

**Section Layout:**
- Header: Full width with gold background
- Left sidebar (0-28% width):
  - Skills
  - Hobbies
- Middle/Right (28-100% width):
  - Education
  - Projects
  - Experience

---

## Template 10 - Modern Gradient
**Layout:** Split two-column
**Font:** Calibri
**Style:** Modern, colorful, creative
**Colors:** Purple gradient header, split background
**Best for:** Creative industries

**Section Layout:**
- Header: Purple gradient full width (0-16%)
- Left section (gray background):
  - Experience
  - Projects
  - Hobbies
- Right section (white background):
  - Education
  - Skills

---

## Template Selection Distribution

With `random.seed(100)`, each resume gets randomly assigned:
- **Random distribution**: ~100 resumes per template
- **Ensures diversity**: CNN sees varied layouts during training
- **Template ID tracking**: Available in filename for analysis

## Visual Diversity Matrix

| Feature | T01 | T02 | T03 | T04 | T05 | T06 | T07 | T08 | T09 | T10 |
|---------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Columns | 1   | 2   | 2   | 1   | 1   | 1   | 1   | 1   | 3   | 2   |
| Header% | 12  | 15  | 15  | 20  | 18  | 10  | 13  | 12  | 14  | 16  |
| Colored | No  | Yes | Yes | Yes | No  | No  | Yes | Yes | Yes | Yes |
| Font    | Sans| Sans| Serif| Sans| Sans| Sans| Sans| Mono| Serif| Sans|
| Spacing | Med | Med | Med | Med | High| Low | Med | Med | Med | Med |

## CNN Training Implications

**Why template diversity matters:**

1. **Layout Variations**: 1-3 columns test spatial understanding
2. **Color Schemes**: 5 colored vs 5 plain test color invariance
3. **Font Variations**: 3 font families test OCR robustness
4. **Spacing**: Dense vs sparse tests boundary detection
5. **Section Order**: 10 different orderings test semantic understanding

**Annotation Challenges:**

- Single-column: Simple vertical bounding boxes
- Multi-column: Overlapping X-coordinates
- Variable header sizes: 10-20% height range
- Different section priorities: Skills-first vs Projects-first

This diversity ensures the CNN learns **layout-agnostic** denoising.
