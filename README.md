\# AI Course Recommender for KCSE Graduates



A final year project that helps KCSE graduates find university courses they qualify for, and (in progress) ranks them by how likely the student is to be satisfied.



\## Current status

\- Eligibility engine working: checks grades against course requirements and explains why a course is excluded

\- Flask web app with a grades form and a results page

\- Course requirements are placeholders, to be replaced with real KUCCPS data



\## Planned

\- Survey of Kenyan university students to collect training data

\- Machine learning model that ranks eligible courses by predicted satisfaction

\- MySQL database, explanations for each recommendation, what-if simulator, feedback loop



\## Tech stack

Python, Flask, scikit-learn, pandas, MySQL



\## Run locally

1\. Create and activate a virtual environment

2\. `pip install flask`

3\. `python app.py`

4\. Open http://127.0.0.1:5000

