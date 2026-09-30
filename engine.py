# Converts each KCSE grade into points so grades can be compared
GRADE_POINTS = {
    'A': 12, 'A-': 11, 'B+': 10, 'B': 9, 'B-': 8, 'C+': 7,
    'C': 6, 'C-': 5, 'D+': 4, 'D': 3, 'D-': 2, 'E': 1,
    'none': 0,
}

# Each course lists its minimum mean grade and subject grades.
# NOTE: these requirements are placeholders for the demo.
# They must be replaced with the real KUCCPS figures.
COURSES = [
    {"name": "BSc Computer Science", "field": "Computing",
     "min_mean": "C+", "subjects": {"maths": "C+", "english": "C"}},
    {"name": "BSc Nursing", "field": "Health",
     "min_mean": "C+", "subjects": {"biology": "C+", "chemistry": "C+"}},
    {"name": "Bachelor of Medicine (MBChB)", "field": "Health",
     "min_mean": "B+", "subjects": {"biology": "B+", "chemistry": "B+"}},
    {"name": "BSc Civil Engineering", "field": "Engineering",
     "min_mean": "B", "subjects": {"maths": "B", "physics": "B"}},
    {"name": "Bachelor of Commerce", "field": "Business",
     "min_mean": "C+", "subjects": {"maths": "C", "english": "C+"}},
    {"name": "Bachelor of Education (Arts)", "field": "Education",
     "min_mean": "C+", "subjects": {"english": "C+", "kiswahili": "C+"}},
    {"name": "BSc Agriculture", "field": "Agriculture",
     "min_mean": "C+", "subjects": {"biology": "C", "chemistry": "C"}},
    {"name": "Bachelor of Laws (LLB)", "field": "Law",
     "min_mean": "B", "subjects": {"english": "B", "kiswahili": "C+"}},
]


def check_eligibility(student):
    """Checks a student's grades against every course.
    Returns one result per course with a yes/no and the reasons."""
    results = []
    for course in COURSES:
        reasons = []

        # Check the mean grade first
        if GRADE_POINTS[student["mean_grade"]] < GRADE_POINTS[course["min_mean"]]:
            reasons.append(f"Mean grade is below {course['min_mean']}")

        # Then check each required subject
        for subject, min_grade in course["subjects"].items():
            if GRADE_POINTS[student[subject]] < GRADE_POINTS[min_grade]:
                reasons.append(f"{subject.capitalize()} is below {min_grade}")

        results.append({
            "name": course["name"],
            "field": course["field"],
            "eligible": len(reasons) == 0,
            "reasons": reasons,
        })
    return results