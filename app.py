import streamlit as st
from resume_parser import extract_text_from_pdf, extract_cgpa
from skill_extractor import extract_skills
from similarity_engine import compute_similarity
from scoring import calculate_skill_match, normalize_cgpa, final_score
from database import init_db, insert_result, get_ranked_results
init_db()

st.title("🎓 AI Smart Campus Placement Screening System")

job_desc = st.text_area("Enter Company Job Description")

uploaded_file = st.file_uploader("Upload Student Resume (PDF)", type=["pdf"])
student_name = st.text_input("Student Name")

if st.button("Evaluate Candidate"):

    if uploaded_file and job_desc:

        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        resume_text = extract_text_from_pdf("temp.pdf")
        cgpa = extract_cgpa(resume_text)

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_desc)

        similarity = compute_similarity(resume_text, job_desc)

        skill_match, missing_skills = calculate_skill_match(
            resume_skills, job_skills
        )

        cgpa_score = normalize_cgpa(cgpa)

        score = final_score(similarity, skill_match, cgpa_score)

        insert_result(student_name, score, missing_skills)

        st.success(f"Final Match Score: {round(score*100, 2)}%")
        st.write("Missing Skills:", missing_skills)


st.subheader("📊 Ranked Students")
results = get_ranked_results()
for rank, row in enumerate(results, 1):

    score = row[1]

    try:
        score = float(score)
    except:
        score = 0

    st.write(f"Rank {rank}: {row[0]} — {round(score*100,2)}%")