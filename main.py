from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/")
def home():
    with open("templates/register.html", "r") as file:
        return file.read()
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll_no TEXT,
    department TEXT,
    dob TEXT,
    email TEXT,
    phone TEXT,
    address TEXT
)
""")

conn.commit()
conn.close()

print("Database and table created successfully!")

@app.post("/register")
def register(
    name: str = Form(...),
    roll_no: str = Form(...),
    department: str = Form(...),
    dob: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    address: str = Form(...)
):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, roll_no, department, dob, email, phone, address) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (name, roll_no, department, dob, email, phone, address)
    )

    conn.commit()
    conn.close()

    return {"message": "Student Registered Successfully"}


@app.get("/students")
def view_students(request: Request):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    return templates.TemplateResponse(
        request=request,
        name="students.html",
        context={"students": students}
    )


@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    conn.close()

    if student:
        return student

    return {"message": "Student not found"}

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    name: str,
    roll_no: str,
    department: str,
    dob: str,
    email: str,
    phone: str,
    address: str
):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET name=?, roll_no=?, department=?, dob=?, email=?, phone=?, address=?
        WHERE id=?
    """, (name, roll_no, department, dob, email, phone, address, student_id))

    conn.commit()
    conn.close()

    return {"message": "Student Updated Successfully"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))

    conn.commit()
    conn.close()

    return {"message": "Student Deleted Successfully"}