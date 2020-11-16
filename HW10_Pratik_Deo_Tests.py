import unittest
from HW10_Pratik_Deo import Respository
from HW10_Pratik_Deo import Student
from HW10_Pratik_Deo import Instructor
import os
import sys
from prettytable import PrettyTable


class Test_student(unittest.TestCase):
    def test_class_student(self):
        student = Student("123456", "Abhimanya Rai", "SSW")
        self.assertEqual(student.s_major, "SSW")
        self.assertEqual(student.s_cwid, "123456")
        self.assertEqual(student.s_name, "Abhimanya Rai")


class TestInstructor(unittest.TestCase):
    def test_instructor(self):
        inst = Instructor("90873", "Rakhi M", "SSW")
        self.assertEqual(inst.i_name, "Rakhi M")
        self.assertEqual(inst.dept, "SSW")
        self.assertEqual(inst.i_courses, {})


class RepoTest(unittest.TestCase):
    repo = Respository("/Users/pratikdeo/Documents/Student-Repository-SSW810")
    expect = ['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']], [
        'SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]
    output = []
    for std in repo.majors.values():
        output.append(std.dept)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
