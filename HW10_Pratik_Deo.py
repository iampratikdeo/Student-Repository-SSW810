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

    def add_the_courses(self, course, grade):
        grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']
        if grade in grades:
            self.s_courses[course] = grade
        elif grade == 'F':
            print(f"Student with id {self.s_cwid} has failed in {course}")
        else:
            print(
                f"Student with id {self.s_cwid} has no grade in {course}")


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

        except FileNotFoundError:
            print("pass the correct path")

        if ptable:
            self.prettytable_student()
            self.prettytable_instructor()

    def prettytable_student(self):
        pt = PrettyTable(
            field_names=['CWID', 'Name', 'Major', 'Completed Courses'])
        for student in self.student.values():
            pt.add_row([student.s_cwid, student.s_name, student.s_major,
                        sorted(student.s_courses.keys())])

        print(pt)

    def get_the_students(self, path):
        try:
            for c, n, m in file_reader(path, 3, sep='\\t', header=False):
                self.student[c] = Student(c, n, m)
        except FileNotFoundError as e1:
            print(f"this is e1: {e1}")
        except ValueError as v:
            print(f"this is v: {v}")

    def get_the_grades(self, path):
        try:
            for cwid, co, gr, Iid in file_reader(path, 4, sep='\\t', header=False):
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
            for c, n, m in file_reader(path, 3, sep='\\t', header=False):
                self.instructors[c] = Instructor(c, n, m)
        except FileNotFoundError as e1:
            print(f"this is e1: {e1}")
        except ValueError as v:
            print(f"this is v: {v}")

    def prettytable_instructor(self):
        pt_2 = PrettyTable(
            field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
        for Instructor in self.instructors.values():
            for cours in Instructor.i_courses:
                pt_2.add_row(
                    [Instructor.i_cwid, Instructor.i_name, Instructor.dept, cours, Instructor.i_courses[cours]])

        print(pt_2)


stevens = Respository("/Users/pratikdeo/Documents/SSW810-HW9/HW9")
