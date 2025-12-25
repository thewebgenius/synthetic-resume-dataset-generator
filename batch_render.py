import json
import random
from pathlib import Path

# Set seed for reproducibility
random.seed(100)

TEMPLATES_DIR = Path("templates")
DATA_PATH = Path("data/resumes")
OUTPUT_DIR = Path("output/html")

def render_all_resumes():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    resume_files = sorted(list(DATA_PATH.glob("*.json")))

    for idx, resume_file in enumerate(resume_files, start=1):
        # Randomly assign template from 1 to 10
        template_id = random.randint(1, 10)
        template_path = TEMPLATES_DIR / f"template_{template_id:02d}" / "resume.html"
        # Randomly assign template from 1 to 10
        template_id = random.randint(1, 10)
        template_path = TEMPLATES_DIR / f"template_{template_id:02d}" / "resume.html"

        # Load resume data
        with open(resume_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Load template
        with open(template_path, "r", encoding="utf-8") as f:
            html = f.read()

        # Personal Info
        html = html.replace("{{name}}", data["personal_info"]["name"])
        html = html.replace("{{job_title}}", data["personal_info"]["job_title"])
        html = html.replace("{{email}}", data["personal_info"]["email"])
        html = html.replace("{{phone}}", data["personal_info"]["phone"])
        html = html.replace("{{linkedin}}", data["personal_info"]["linkedin"])
        html = html.replace("{{github}}", data["personal_info"]["github"])

        # Summary
        html = html.replace("{{summary}}", data["summary"])

        # Education
        edu = data["education"][0]
        education_html = f"""
        <p>
            {edu['degree']} in {edu['field']}<br>
            {edu['institution']} ({edu['start_year']}–{edu['end_year']})
        </p>
        """

        # Skills - Categorized
        skills_html = "<div class='skills-grid'>"
        for category, skills_list in data["skills"].items():
            category_name = category.replace("_", " & ").title()
            skills_html += f"<div class='skill-category'><strong>{category_name}:</strong> {', '.join(skills_list)}</div>"
        skills_html += "</div>"

        # Projects with bullet points
        projects_html = ""
        for p in data["projects"]:
            projects_html += f"<div class='project'><strong>{p['title']}</strong><ul>"
            for bullet in p['description']:
                projects_html += f"<li>{bullet}</li>"
            projects_html += "</ul></div>"

        # Experience with bullet points
        experience_html = "<div class='experience'>"
        for bullet in data["experience"]:
            experience_html += f"<li>{bullet}</li>"
        experience_html = "<ul>" + experience_html + "</ul></div>"

        # Hobbies
        hobbies_html = ", ".join(data["hobbies"])

        # Replace placeholders
        html = html.replace("{{education}}", education_html)
        html = html.replace("{{skills}}", skills_html)
        html = html.replace("{{projects}}", projects_html)
        html = html.replace("{{experience}}", experience_html)
        html = html.replace("{{hobbies}}", hobbies_html)

        # Output file with template ID encoded in filename
        output_file = OUTPUT_DIR / f"resume_{idx:04d}_t{template_id:02d}.html"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"Generated: {output_file.name} (Template {template_id:02d})")

if __name__ == "__main__":
    render_all_resumes()
