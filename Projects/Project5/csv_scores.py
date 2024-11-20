# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477
import csv

def read_csv(fname):
    try:
        with open(fname, "r") as file:
            read_file = csv.reader(file)
            r_list = []
            for row in read_file:
                name = row[0]
                section = row[1]
                scores = [float(score) for score in row[2:]]
                average = round(sum(scores) / len(scores), 3)
                student_dict = {
                    'name': name,
                    'section': section,
                    'scores': scores,
                    'average': average
                }
                r_list.append(student_dict)
            return r_list if r_list else None
    except (FileNotFoundError, IsADirectoryError):
        print(f"Error occurred when opening {fname} to read")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def write_csv(fname, student_data):
    try:
        with open(fname , 'w' , newline= '') as file:
            witer = csv.write(file)
            for student in student_data:
                row = [student['name'], student['section'] + student['scores']]


























