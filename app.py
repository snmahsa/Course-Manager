from flask import Flask, render_template, request, redirect
from data import courses_list, student_info
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', course = courses_list)


if __name__ == "__main__":
    app.run(debug=True)