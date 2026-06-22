## Student Registration System

## Project Overview

The Student Registration System is a web-based application developed using FastAPI and SQLite. It allows users to manage student records efficiently through a simple interface.

## Features

* Add new student records
* View all registered students
* Update student information
* Delete student records
* Store data using SQLite database
* User-friendly web interface

## Technologies Used

* Python
* FastAPI
* SQLite3
* HTML
* Jinja2 Templates
* Uvicorn

## Project Structure
Student_Registration_System/

├── main.py

├── database.db

├── templates/

│   ├── index.html

│   ├── students.html

│   └── edit.html

└── README.md

## Installation

1. Clone the repository:

git clone https://github.com/dharshini1301/Student_Registration_System.git

2. Navigate to the project directory:

cd Student_Registration_System

3. Install dependencies:

pip install fastapi uvicorn jinja2

4. Run the application:

uvicorn main:app --reload

5. Open your browser:

http://127.0.0.1:8000

## Database

The application uses SQLite as the database. Student information is stored in the `database.db` file.

## CRUD Operations

* Create: Add new student details
* Read: View student records
* Update: Modify existing student details
* Delete: Remove student records

## Author

Dharshini T

## Future Enhancements

* Student search functionality
* Authentication and login system
* Improved user interface
* Export student records to Excel/PDF
