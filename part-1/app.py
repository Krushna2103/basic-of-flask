"""
Part 1: Hello Flask - Your First Web Server
============================================
Updated using comments & exercises

Changes made:
1. Personalized welcome message
2. HTML response instead of plain text
3. Added /about route
"""

# ============================================================================
# IMPORTS
# ============================================================================
from flask import Flask


# ============================================================================
# APPLICATION SETUP
# ============================================================================
app = Flask(__name__)
# __name__ helps Flask locate templates & static files


# ============================================================================
# ROUTES
# ============================================================================

@app.route('/')
def home():
    """
    Home page route
    Returns HTML instead of plain text
    """
    return """
    <h1>Hello Krushna!</h1>
    <p>Welcome to my first Flask web server 🚀</p>
    <p>This page is rendered using HTML.</p>
    """


@app.route('/about')
def about():
    """
    About page route
    """
    return """
    <h2>About This App</h2>
    <p>This is a beginner Flask application.</p>
    <p>Created by Krushna Dnyaneshwar Kharade.</p>
    """


# ============================================================================
# APPLICATION ENTRY POINT
# ============================================================================

if __name__ == '__main__':
    # debug=True enables auto-reload & error details
    app.run(debug=True)
