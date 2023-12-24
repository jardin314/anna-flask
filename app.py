"""
TODO pydoc
"""


from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)


@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def admin():
    return render_template('contact')


if __name__ == '__main__':
    app.run()
