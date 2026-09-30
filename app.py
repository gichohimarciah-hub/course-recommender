from flask import Flask, render_template, request
from config import Config
from engine import check_eligibility

app = Flask(__name__)
app.config.from_object(Config)

# These are the form fields the engine needs, in one place
FIELDS = ["mean_grade", "maths", "english", "kiswahili",
          "biology", "chemistry", "physics", "geography"]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    # Read each grade the student chose in the form
    student = {field: request.form[field] for field in FIELDS}

    # Run the eligibility engine, then split the results into two groups
    results = check_eligibility(student)
    eligible = [r for r in results if r["eligible"]]
    not_eligible = [r for r in results if not r["eligible"]]

    return render_template('recommendations.html',
                           eligible=eligible,
                           not_eligible=not_eligible)


if __name__ == '__main__':
    app.run(debug=True)