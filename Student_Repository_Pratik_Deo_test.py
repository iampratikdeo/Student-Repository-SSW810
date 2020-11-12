import unittest
import datetime
from HW08_Pratik_Deo import file_reader, FileAnalyzer, date_arithmetic


class test_lists(unittest.TestCase):

    def test_date_arithmetic(self) -> None:
        """test cases for date arithmetic"""
        value: tuple = date_arithmetic()
        correct: tuple = (datetime.date(2020, 3, 1),
                          datetime.date(2019, 3, 2), 241)
        self.assertTupleEqual(value, correct)
        self.assertNotEqual(value, '')

    def test_file_reader(self) -> None:
        """test cases for file reader"""
        value: list = [('123', 'Jin He', 'Computer Science'), ('234', 'Nanda Koka',
                                                               'Software Engineering'), ('345', 'Benji Cai', 'Software Engineering')]
        value2: list = [('CWID', 'Name', 'Major'), ('123', 'Jin He', 'Computer Science'), (
            '234', 'Nanda Koka', 'Software Engineering'), ('345', 'Benji Cai', 'Software Engineering')]
        self.assertEqual([a for a in file_reader(
            "/Users/pratikdeo/Documents/SSW 810 Fall 2020/HW8/student_majors.txt", 3, "|", True)], value)
        self.assertEqual([a for a in file_reader(
            "/Users/pratikdeo/Documents/SSW 810 Fall 2020/HW8/student_majors.txt", 3, "|", False)], value2)

    def test_file_analyzer(self) -> None:
        """test case for file analyzer """
        correct = {'/Users/pratikdeo/Documents/SSW 810 Fall 2020/HW1HW1_pratikdeo.py': {
            'class': 0, 'function': 0, 'line': 58, 'char': 1445}}
        self.assertEqual(FileAnalyzer(
            "/Users/pratikdeo/Documents/SSW 810 Fall 2020/HW1").files_summary, correct)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
