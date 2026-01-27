"""
Part 2: Templates - Rendering HTML Files
=======================================
This file demonstrates how to render HTML templates using Flask.

How to Run:
1. Activate virtual environment (if any)
2. Run: python app.py
3. Open browser and visit:
   http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)


# Home Page Route
@app.route('/')
def home():
    # Renders templates/index.html
    return render_template('index.html')


# About Page Route
@app.route('/about')
def about():
    # Renders templates/about.html
    return render_template('about.html')


# Contact Page Route (Exercise 2.2)
@app.route('/contact')
def contact():
    # Renders templates/contact.html
    return render_template('contact.html')


# Main entry point
if __name__ == '__main__':
    app.run(debug=True)


"""
FOLDER STRUCTURE (Part 2)
------------------------
part-2/
│
├── app.py
│
└── templates/
    ├── index.html
    ├── about.html
    └── contact.html

EXERCISES STATUS
----------------
Exercise 2.1: Modify templates            ✅ Completed
Exercise 2.2: Create Contact page         ✅ Completed
Exercise 2.3: Add navigation links        ✅ Completed
"""
