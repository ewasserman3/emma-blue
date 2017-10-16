from flask import Flask, render_template
import datetime
import os
 
 
application = Flask(__name__)


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


@application.route("/main")
def main_site():
    return render_template('index.html', tabs=tabs)


@application.route("/")
def landing_page():
    return render_template('landing-page.html', tabs=tabs)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0', port=port, debug=True, use_reloader=True))
