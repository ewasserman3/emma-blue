from flask import Flask, render_template
import os
 
 
app = Flask(__name__)


tabs = [
    {
        'name': 'Work',
        'index': 'work',
        'template': 'work.html'
    },
    {
        'name': 'About',
        'index': 'about',
        'template': 'about.html'
    },
    {
        'name': 'Support',
        'index': 'support',
        'template': 'support.html'
    },
    {
        'name': 'Contact',
        'index': 'contact',
        'template': 'contact.html'
    }
]


@app.route("/main")
def main_site():
    return render_template('index.html', tabs=tabs)


@app.route("/")
def landing_page():
    return render_template('landing-page.html', tabs=tabs)


@app.route("/new")
def test_page():
    return render_template('new.html', tabs=tabs)


if __name__ == "__main__":
    app.run(debug=True)
