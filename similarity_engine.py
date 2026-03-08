from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text):
    return model.encode([text])[0]


def compute_similarity(resume_text, job_desc):
    resume_emb = get_embedding(resume_text)
    job_emb = get_embedding(job_desc)

    similarity = cosine_similarity(
        [resume_emb], [job_emb]
    )[0][0]

    return similarity
