from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# PERSONAL DATA
# =============================================================================
PERSONAL_INFO = {
    'name': 'KHARADE KRUSHNA',
    'title': 'Web Developer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'kharadekrushna03.email@example.com',
    'github': 'https://github.com/krushna2103',
    'linkedin': 'https://linkedin.com/in/yourusername',
}

SKILLS = [
    {'name': 'Python', 'level': 80},
    {'name': 'HTML/CSS', 'level': 75},
    {'name': 'Flask', 'level': 60},
    {'name': 'JavaScript', 'level': 50},
    {'name': 'SQL', 'level': 45},
]

PROJECTS = [
    {
        'id': 1,
        'name': 'Personal Website',
        'description': 'A Flask-powered personal portfolio website.',
        'tech': ['Python', 'Flask', 'HTML', 'CSS'],
        'status': 'Completed'
    },
    {
        'id': 2,
        'name': 'Todo App',
        'description': 'A simple task management application.',
        'tech': ['Python', 'Flask', 'SQLite'],
        'status': 'In Progress'
    },
    {
        'id': 3,
        'name': 'Weather Dashboard',
        'description': 'Display weather data from an API.',
        'tech': ['Python', 'Flask', 'API'],
        'status': 'Planned'
    },
]

# =============================================================================
# ROUTES
# =============================================================================
@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    return render_template(
        'project_detail.html',
        info=PERSONAL_INFO,
        project=project,
        project_id=project_id
    )


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)


if __name__ == '__main__':
    app.run(debug=True)
