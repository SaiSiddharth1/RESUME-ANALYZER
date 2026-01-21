from app.models.ml_models import nlp

KNOWN_SKILLS = {
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "SQL",
    "Machine Learning",
    "Data Analysis",
    "Project Management",
    "Communication",
    "Leadership",
    "fastapi", "django",
    "react", "javascript", "sql", "postgresql",
    "docker", "aws", "git"
}

def extract_skills(text : str) -> list[str]:
    doc = nlp(text.lower())
    skills = set()

    for token in doc:
        if token.text in KNOWN_SKILLS:
            skills.add(token.text)
    return list(skills)
        
