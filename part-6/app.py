"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data - your tasks list
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

# Counter for generating new IDs
next_id = 4

# Route 1: Home page - display all tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=TASKS)

# Route 2: Add task page with form
@app.route('/add', methods=['GET', 'POST'])
def add():
    global next_id
    if request.method == 'POST':
        title = request.form.get('title')
        status = request.form.get('status', 'Pending')
        priority = request.form.get('priority', 'Medium')
        
        if title:
            new_task = {
                'id': next_id,
                'title': title,
                'status': status,
                'priority': priority
            }
            TASKS.append(new_task)
            next_id += 1
            return redirect(url_for('index'))
    
    return render_template('add.html')

# Route 3: View single task details
@app.route('/task/<int:id>')
def task_detail(id):
    task = None
    for t in TASKS:
        if t['id'] == id:
            task = t
            break
    
    if task is None:
        return "Task not found", 404
    
    return render_template('task.html', task=task)

# Route 4: About page
@app.route('/about')
def about():
    return render_template('about.html')

# Bonus: Filter by priority
@app.route('/priority/<name>')
def priority_filter(name):
    priority_tasks = [task for task in TASKS if task['priority'].lower() == name.lower()]
    return render_template('index.html', tasks=priority_tasks, filter_name=f"Priority: {name}")


if __name__ == '__main__':
    app.run(debug=True)
