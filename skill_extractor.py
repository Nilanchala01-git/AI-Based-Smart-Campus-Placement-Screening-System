SKILL_DB = [
    "python","java","c++","machine learning","deep learning","nlp",
    "sql","react","docker","aws","tensorflow","pytorch"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILL_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))