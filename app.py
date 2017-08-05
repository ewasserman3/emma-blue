from flask import Flask, render_template
 
 
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
 
@app.route("/test")
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
