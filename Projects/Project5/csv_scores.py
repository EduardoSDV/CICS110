# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477
import csv
import statistics
import os

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
        with open(fname, 'w', newline='') as file:
            writer = csv.writer(file)

            for student in student_data:
                name = student['name']
                section = student['section']
                scores = student['scores']

                scores_str = ",".join(map(str, scores))

                row = f"{name},{section},{scores_str}"
                writer.writerow(row.split(","))


    except Exception as e:
        print(f"Error occurred when opening {fname} to write")
        return

def filter_section(student_data, section_name):
    return [hashmap for hashmap in student_data if hashmap.get('section') == section_name]

def filter_average(student_data ,min_inc ,max_exc ):

    return [hashmap for hashmap in student_data if min_inc < statistics.mean(hashmap.get('scores')) <= max_exc]

def split_section(fname):
    student_data = read_csv(fname)
    if student_data is None:
        return None
    name_file = os.path.splitext(fname)[0]

    unique_sections = set(student['section'] for student in student_data)

    for section in unique_sections:
        section_data = filter_section(student_data, section)
        output_fname = f"{name_file}_section_{section}.csv"
        write_csv(output_fname, section_data)














































