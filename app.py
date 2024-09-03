from flask import Flask, render_template, request, redirect
from data import courses_list, student_info
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['POST','GET'])
def profile():
    if request.method == 'POST':
        student_info['name'] = request.form['name']
        student_info['email'] = request.form['email']
        student_info['major'] = request.form['major']

    return render_template('profile.html',student =student_info)














if __name__ == "__main__":
    app.run(debug=True)