import json
from pathlib import Path

# Paths
TEMPLATE_PATH = Path("templates/template_1/resume.html")
OUTPUT_PATH = Path("output/html/rendered_resume.html")

# Pick the first resume JSON file
RESUME_JSON = list(Path("data/resumes").glob("*.json"))[0]

def render_resume():
    # Load resume JSON
    with open(RESUME_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Load HTML template
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # Personal info
    html = html.replace("{{name}}", data["personal_info"]["name"])
    html = html.replace("{{email}}", data["personal_info"]["email"])
    html = html.replace("{{phone}}", data["personal_info"]["phone"])

    # Education
    edu = data["education"][0]
    education_html = f"""
    <p>
        {edu['degree']} in {edu['field']}<br>
        {edu['institution']} ({edu['start_year']}–{edu['end_year']})
    </p>
    """

    # Skills
    skills = (
        data["skills"]["programming"]
        + data["skills"]["ml_ai"]
        + data["skills"]["tools"]
    )
    skills_html = "<ul>" + "".join(f"<li>{s}</li>" for s in skills) + "</ul>"

    # Projects
    projects_html = ""
    for p in data["projects"]:
        projects_html += f"""
        <p>
            <strong>{p['title']}</strong><br>
            {p['description']}
        </p>
        """

    # Experience
    if data["experience"]:
        e = data["experience"][0]
        experience_html = f"""
        <p>
            {e['role']} – {e['company']} ({e['duration_months']} months)
        </p>
        """
    else:
        experience_html = "<p>—</p>"

    # Hobbies
    hobbies_html = ", ".join(data["hobbies"])

    # Replace placeholders
    html = html.replace("{{education}}", education_html)
    html = html.replace("{{skills}}", skills_html)
    html = html.replace("{{projects}}", projects_html)
    html = html.replace("{{experience}}", experience_html)
    html = html.replace("{{hobbies}}", hobbies_html)

    # Save output
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html)

    print("Rendered resume saved at:", OUTPUT_PATH)

if __name__ == "__main__":
    render_resume()
