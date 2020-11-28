from flask import Flask, render_template
from typing import List, Dict
import sqlite3
db_file: str = "/Users/pratikdeo/Documents/Student-Repository-SSW810/hw11/hw11.db"


app: Flask = Flask(__name__)


@app.route('/pratikdeo')
def completed_couses() -> str:
    query: str = """select students.Name as Name, students.CWID as CWID, grades.Course, grades.Grade, instructors.Name as Instructor_Name 
                    from students, grades, instructors
                    where students.CWID = grades.StudentCWID  and  grades.InstructorCWID = instructors.CWID order by students.Name"""

    db: sqlite3.Connection = sqlite3.connect(db_file)
    data: Dict[str, str] = [{'cwid': cwid, 'name': name, 'course': course, 'grade': grade, 'Intructor_Name': i_name}
                            for name, cwid, course, grade, i_name in db.execute(query)]
    db.close()
    return render_template('1.html', title="Stevens repository", table_title="Student with grades and professor",
                           students=data)


app.run(debug=True)
