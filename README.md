
## Project: Course-Manager
Simple Project about MLOps (Flask + HTML + CSS )

### Introduction
The "Student Portal" project is a web application built using the Flask framework. It is designed to create an educational portal for students and teachers. This portal includes various features such as viewing user profile, managing and displaying courses, and adding new courses by teachers.

### Project Goals
- To create an educational portal for managing student and course information.
- To provide a simple and user-friendly interface for viewing and managing courses.
- To utilize modern web technologies and the Flask framework for development and implementation.

### Features
1. Home Page:
   - Display a welcome message and navigation to different pages.

2. Profile Page:
   - Display student profile information including name, email, and major.
   - Allow updating of profile information through a form.

3. Courses Page:
   - Display a list of available courses with descriptions and teacher names.
   - Use HTML tables to display the list of courses neatly.

4. Add Course:
   - Provide a form for teachers to add new courses.
   - Validate the form to ensure all necessary fields are filled.
   - Add new courses to the list of courses and display them on the courses page.

5. Course Details:
   - Display the details of each course individually using dynamic URLs.

### Project Structure
The project includes the following directories and files:
project_name/ │ ├── app/ │   ├── init.py │   ├── routes.py │   ├── models.py │   ├── forms.py │   ├── templates/ │   │   ├── base.html │   │   ├── index.html │   │   ├── profile.html │   │   ├── courses.html │   │   ├── add_course.html │   │   └── course_detail.html │   └── static/ │       ├── css/ │       │   └── styles.css │       ├── js/ │       │   └── main.js │       └── img/ │           └── logo.png │ ├── config.py ├── run.py ├── requirements.txt └── instance/ └── config.py

  
