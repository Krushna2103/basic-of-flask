"""
Part 3: Jinja2 Variables - Passing Data from Python to HTML
============================================================
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    student_name = "Alex"
    return render_template('index.html', name=student_name)


@app.route('/profile')
def profile():
    user_data = {
        'name': 'Sarah',
        'age': 22,
        'course': 'Web Development',
        'email': 'sarah@gmail.com',   # Exercise 3.1
        'city': 'Pune',               # Exercise 3.1
        'is_enrolled': True
    }

    return render_template(
        'profile.html',
        name=user_data['name'],
        age=user_data['age'],
        course=user_data['course'],
        email=user_data['email'],
        city=user_data['city'],
        is_enrolled=user_data['is_enrolled']
    )


@app.route('/skills')
def skills():
    programming_skills = ['Python', 'HTML', 'CSS', 'JavaScript', 'Flask']
    return render_template('skills.html', skills=programming_skills)


@app.route('/projects')
def projects():
    project_list = [
        {'name': 'Personal Website', 'status': 'Completed', 'tech': 'HTML/CSS'},
        {'name': 'Flask Blog', 'status': 'In Progress', 'tech': 'Python/Flask'},
        {'name': 'Weather App', 'status': 'Planned', 'tech': 'JavaScript'},
    ]
    return render_template('projects.html', projects=project_list)


# ✅ Exercise 3.3 — Grades Page
@app.route('/grades')
def grades():
    student_grades = {
        'Mathematics': 'A',
        'Python': 'A+',
        'Web Technology': 'A',
        'Data Structures': 'B+'
    }
    return render_template('grades.html', grades=student_grades)


if __name__ == '__main__':
    app.run(debug=True)
