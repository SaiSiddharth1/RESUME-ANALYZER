from sklearn.metrics.pairwise import cosine_similarity
from app.models.ml_models import embedding_model

def calculate_match_score(resume_text: str,job_text: str)->float:
    embeddings = embedding_model.encode([resume_text,job_text])
    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
        )
    return round(float(similarity[0][0])*100,2)

def find_missing_skills(
        resume_skills : list[str],
        job_skills : list[str]
)->list[str]:
    return list(set(job_skills) - set(resume_skills))

