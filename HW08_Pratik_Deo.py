import os
from datetime import datetime, timedelta
from typing import Tuple, Iterator, List
from prettytable import PrettyTable


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """This function performs three date operations """
    # 1. An instance of  class datetime representing the date three days after Feb 27, 2020.
    three_days_after_02272020: datetime = (datetime(
        2020, 2, 27) + timedelta(days=3)).date()
    # 2. An instance of  class datetime representing the date three days after Feb 27, 2019.
    three_days_after_02272019: datetime = (datetime(
        2019, 2, 27) + timedelta(days=3)).date()
    # 3. An int representing the number of days between Feb 1, 2019 and Sept 30, 2019
    date1 = datetime(2019, 9, 30)
    date2 = datetime(2019, 2, 1)
    diff = date1 - date2
    return three_days_after_02272020, three_days_after_02272019, diff.days


def file_reader(path, fields, sep, header) -> Iterator[List[str]]:
    """file_reader function that reads file which have a separator"""
    try:
        # Trying to open the file
        f = open(path, "r")
    except FileNotFoundError:
        # Raise error if file is not found
        raise FileNotFoundError
    else:
        with f:
            if header == True:
                next(f)
                # enumerating over the file
            for i, line in enumerate(f):
                # removes the leading and trailing spaces from the current line
                current_line = line.strip()
                # split the current line on the basis of the separator
                current_line = current_line.split(sep)
                # check if the length of current line after spliting is more than specified fields then error out
                if(len(current_line) == fields):
                    yield tuple(line.strip().split(sep))
                else:
                    raise ValueError(
                        f"{f} has {len(current_line)} on line {i + 1} and {fields}")


class FileAnalyzer:
    """ Class to implement analyze_filers, pretty_print functions """

    def __init__(self, directory):
        """ Function to initalizes variable directory """
        self.directory = directory
        self.files_summary = self.analyze_files()

    def analyze_files(self):
        """ Function to count number of lines, characters, functions and classes in a file """
        self.list_d = dict()
        try:
            list_files = os.listdir(self.directory)
        except FileExistsError:
            raise FileExistsError("not found")
        else:
            for file in list_files:
                # identifying .py files
                if file.endswith(".py"):
                    try:
                        fp = open(os.path.join(self.directory, file), "r")
                    except FileNotFoundError:
                        raise FileNotFoundError("Cant find file pls")
                    else:
                        with fp:
                            num_lines, num_char, num_func, num_class = 0, 0, 0, 0
                            file_name = self.directory + file
                            for line in fp:
                                # counting number of lines
                                line = line.strip()
                                num_lines += 1
                                # counting number of characters
                                num_char = num_char + len(line)
                                # counting number of definitions
                                if line.startswith("def ") and line.endswith(":"):
                                    num_func += 1
                                # counting number of classes
                                elif line.startswith("class ") and line.endswith(":"):
                                    num_class += 1
                        self.list_d[file_name] = {
                            "class": num_class, "function": num_func, "line": num_lines, "char": num_char}
        return self.list_d

    def pretty_print(self):
        """ To print the file summary in a pretty table"""
        pretty_table = PrettyTable(
            field_names=["File Name", "Classes", "Functions", "Lines", "Characters"])

        for file_name in self.list_d:
            pretty_table.add_row([file_name, self.list_d[file_name]["class"], self.list_d[file_name]
                                  ["function"], self.list_d[file_name]["line"], self.list_d[file_name]["char"]])

        return pretty_table


if __name__ == "__main__":
    file_reader("/Users/pratikdeo/Documents/SSW810-HW9/HW9/students.txt",
                3, sep='  ', header=True)
