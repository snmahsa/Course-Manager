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


@app.route('/courses')
def courses():
    return render_template('courses_page.html',courses_list = courses_list )


@app.template_filter('limit')
def limit(s):
    splited =s.split()[:1]
    return "".join(splited) + '...'

@app.route('/add_course' ,methods=['POST',"GET"])
def add_course():
    name = request.form['name']
    teacher = request.form['teacher']
    description = request.form['description']
    if not name or not teacher or not description :
        return redirect('/errors')
    
    courses_len = len(courses_list)
    courses_list.append({"id":courses_len + 1 , "name" : name , "teacher": teacher, "description":description})
    return redirect('/cources')




if __name__ == "__main__":
    app.run(debug=True)
