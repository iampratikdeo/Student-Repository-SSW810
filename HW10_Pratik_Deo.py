from HW08_Pratik_Deo import file_reader
from prettytable import PrettyTable
import os
from collections import defaultdict


class Student:

    def __init__(self, cwid, name, major):
        self.s_cwid = cwid
        self.s_name = name
        self.s_major = major
        self.s_courses = dict()
        self.s_gpa = 0

    def add_the_courses(self, course, grade):
        grades = ('A', 'A-', 'B+', 'B', 'B-', 'C+', 'C')
        if grade in grades:
            self.s_courses[course] = grade
        elif grade == 'F':
            print(f"Student with id {self.s_cwid} has failed in {course}")
        else:
            print(
                f"Student with id {self.s_cwid} has no grade in {course}")

    def calculate_gpa(self):
        points: [self.grades_map[grade] for grade in self.s_courses.values()]
        return (points)


class Major:
    def __init__(self, dept, R_E, course):
        self.m_dept = dept
        self.required_courses = set()
        self.elective_courses = set()


class Instructor:
    def __init__(self, cwid, name, dept):
        self.i_cwid = cwid
        self.i_name = name
        self.dept = dept
        self.i_courses = defaultdict(int)

    def get_no_of_students(self, course):
        self.i_courses[course] += 1


class Respository:
    def __init__(self, path, ptable=True):
        self.student = dict()
        self.instructors = dict()
        self.majors = dict()
        try:
            self.get_the_students(os.path.join(path, "students.txt"))
            self.get_the_instructors(os.path.join(path, "instructors.txt"))
            self.get_the_grades(os.path.join(path, "grades.txt"))
            self.ge_the_majors(os.path.join(path, "majors.txt"))
        except FileNotFoundError:
            print("pass the correct path")

        if ptable:
            self.prettytable_major()
            self.prettytable_student()
            self.prettytable_instructor()

    def prettytable_student(self):
        pt = PrettyTable(
            field_names=['CWID', 'Name', 'Major', 'Completed Courses', 'Required Courses', 'Elective Courses', 'GPA'])
        grades_map = {'A': 4.0, 'A-': 3.75, 'B+': 3.25, 'B': 3.0,
                      'B-': 2.75, 'C+': 2.25, 'C': 2.0, 'C-': 0, 'D+': 0, 'D-': 0, 'F': 0}
        for student in self.student.values():
            l: list = [grades_map[grade]
                       for grade in student.s_courses.values()]
            if len(l) > 0:
                gpa: float = sum(l)/len(l)
            else:
                gpa = 0.0
            elective_c = list(self.majors[student.s_major].elective_courses)
            student_courses = student.s_courses.keys()
            if(len(elective_c - student_courses) == 3):
                ec = elective_c
            else:
                ec = []
            pt.add_row([student.s_cwid, student.s_name, student.s_major,
                        sorted(student.s_courses.keys()), list(self.majors[student.s_major].required_courses -
                                                               student_courses), ec, round(gpa, 2)])

        print(pt)

    def prettytable_major(self):
        pt_3 = PrettyTable(field_names=['Dept', 'Required', 'Electives'])
        for maj in self.majors.values():
            pt_3.add_row([maj.m_dept, sorted(maj.required_courses),
                          sorted(maj.elective_courses)])
        print(pt_3)

    def get_the_students(self, path):
        try:
            for c, n, m in file_reader(path, 3, sep=';', header=True):
                self.student[c] = Student(c, n, m)
        except FileNotFoundError as e1:
            print(f"this is e1: {e1}")
        except ValueError as v:
            print(f"this is v: {v}")

    def get_the_grades(self, path):
        try:
            for cwid, co, gr, Iid in file_reader(path, 4, sep='|', header=False):
                if cwid in self.student.keys():
                    self.student[cwid].add_the_courses(co, gr)
                else:
                    print("no record")
                if Iid in self.instructors.keys():
                    self.instructors[Iid].get_no_of_students(co)
                else:
                    print("no prof ")
        except ValueError as v:
            print(v)

    def get_the_instructors(self, path):
        try:
            for c, n, m in file_reader(path, 3, sep='|', header=False):
                self.instructors[c] = Instructor(c, n, m)
        except FileNotFoundError as e1:
            print(f"this is e1: {e1}")
        except ValueError as v:
            print(f"this is v: {v}")

    def ge_the_majors(self, path):
        try:
            for d, r_e_c, c in file_reader(path, 3, sep="	", header=True):
                if d not in self.majors.keys():
                    self.majors[d] = Major(d, r_e_c, c)
                if r_e_c.upper() == 'R':
                    self.majors[d].required_courses.add(c)
                elif r_e_c.upper() == "E":
                    self.majors[d].elective_courses.add(c)
        except FileNotFoundError as f:
            print(f)
        except ValueError as v:
            print(v)

    def prettytable_instructor(self):
        pt_2 = PrettyTable(
            field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
        for Instructor in self.instructors.values():
            for cours in Instructor.i_courses:
                pt_2.add_row(
                    [Instructor.i_cwid, Instructor.i_name, Instructor.dept, cours, Instructor.i_courses[cours]])

        print(pt_2)


Respository("/Users/pratikdeo/Documents/Student-Repository-SSW810")
