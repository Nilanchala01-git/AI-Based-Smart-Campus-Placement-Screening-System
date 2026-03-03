# 🎓 AI-Based Smart Campus Placement Screening System

An AI-powered intelligent recruitment screening system that automates campus placement shortlisting using Natural Language Processing (NLP), Transformer-based semantic similarity, and multi-factor scoring.

---

## 🚀 Project Overview

Campus placement cells traditionally shortlist candidates based on:

- CGPA
- Manual resume review
- Basic skill matching

This process is:

- ⏳ Time-consuming
- ⚖ Potentially biased
- 📉 Inconsistent across evaluators

This project introduces an AI-driven smart screening system that:

✔ Automatically parses student resumes (PDF)  
✔ Extracts skills using NLP  
✔ Matches resumes with job descriptions using Sentence-BERT  
✔ Computes eligibility scores  
✔ Identifies skill gaps  
✔ Ranks students automatically  

---

## 🧠 Core AI Concepts Used

- Resume Parsing (PDF text extraction)
- Natural Language Processing (NLP)
- Sentence-BERT Embeddings
- Cosine Similarity
- Multi-factor Weighted Scoring
- Ranking Algorithms
- Database Integration

---

## 🏗️ System Architecture

---

## ⚙️ AI Scoring Formula

The final eligibility score is calculated using a weighted scoring model:


### Why this formula?

- 50% weight to contextual job-resume similarity
- 30% weight to skill coverage
- 20% weight to academic performance

This ensures a balanced, fair, and data-driven evaluation.

---

## 📊 Output Example

| Student | Match Score | Missing Skills | Rank |
|----------|------------|---------------|------|
| A | 87% | AWS, Docker | 1 |
| B | 76% | React | 2 |

---

## 🛠️ Technology Stack

### Backend
- Python

### AI & NLP
- Sentence Transformers
- scikit-learn
- Regular Expressions
- PyMuPDF (PDF parsing)

### Frontend
- Streamlit

### Database
- SQLite

---

## 📁 Project Structure (Single File Version)

---

## 💻 Installation & Setup

### 1️⃣ Clone Repository

### 2️⃣ Install Dependencies

### 3️⃣ Run Application

---

## 📦 requirements.txt

---

## 🎯 Key Features

- 📄 Automatic resume parsing (PDF)
- 🧠 AI-powered semantic job matching
- 📌 Skill gap analysis
- 📊 Smart ranking engine
- 🗂 SQLite-based result storage
- 🌐 Interactive Streamlit dashboard

---

## 📈 Evaluation Metrics (For Academic Validation)

To evaluate system effectiveness:

- Precision
- Recall
- F1-Score
- Ranking Accuracy
- Mean Reciprocal Rank (MRR)

---

## 🔬 Future Enhancements

- Explainable AI (Highlight matched resume sections)
- Bias Detection Module
- Multi-company filtering
- Resume improvement suggestions
- Admin analytics dashboard
- Cloud deployment
- API integration for recruitment systems

---

## 🎓 Academic Contribution

This project demonstrates:

- Real-world NLP application in recruitment
- Transformer-based semantic understanding
- AI-based decision automation
- Ethical considerations in hiring systems
- Practical deployment using Streamlit

Suitable for:

- Final Year B.Tech Project
- Research Publication
- IEEE / Springer Conference Paper
- AI & NLP Portfolio Showcase

---

## 👨‍💻 Developed By

Nilanchala Mahanty  
B.Tech – Computer Science Engineering  
AI & Deep Learning Enthusiast  

---

## 📜 License

This project is developed for academic and research purposes only.

---

## ⭐ Support

If you find this project useful:

- ⭐ Star this repository
- 🔁 Share with peers
- 💡 Contribute improvements

---
