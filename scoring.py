def calculate_skill_match(resume_skills, job_skills):
    
    if len(job_skills) == 0:
        return 0, []

    matched = set(resume_skills) & set(job_skills)
    missing = list(set(job_skills) - matched)

    skill_score = len(matched) / len(job_skills)

    return skill_score, missing


def normalize_cgpa(cgpa):
    return cgpa / 10.0


def final_score(similarity, skill_match, cgpa_score):

    return (
        0.5 * similarity +
        0.3 * skill_match +
        0.2 * cgpa_score
    )