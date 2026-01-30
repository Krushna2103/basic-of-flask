from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ======================================================
# EXERCISE: In-memory task list (no database)
# ======================================================
tasks = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Practice Jinja', 'status': 'Pending', 'priority': 'Low'}
]

# ======================================================
# EXERCISE 1: Display all tasks
# ======================================================
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


# ======================================================
# EXERCISE 2: View single task details
# ======================================================
@app.route('/task/<int:id>')
def task_detail(id):
    task = next((t for t in tasks if t['id'] == id), None)
    return render_template('task.html', task=task)


# ======================================================
# EXERCISE 3: Add new task
# ======================================================
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_task = {
            'id': len(tasks) + 1,
            'title': request.form['title'],
            'status': request.form['status'],
            'priority': request.form['priority']
        }
        tasks.append(new_task)
        return redirect(url_for('index'))

    return render_template('add.html')


# ======================================================
# EXERCISE 4: About page (static content)
# ======================================================
@app.route('/about')
def about():
    return render_template('about.html')


# ======================================================
if __name__ == '__main__':
    app.run(debug=True)