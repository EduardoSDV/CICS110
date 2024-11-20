# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477

def print_stars_to_file(n):
    file_name = f"stars_{n}.txt"

    with open(file_name,"w") as file:
        for i in range(1, n+1):
            spaces = " " * (n-i)
            stars = "*" * (2*  i -1)
            file.write(spaces + stars + "\n")

def calc_avg_from_file():
    grades = []
    n_grades = 0
    with open("grades.txt" , "r") as file:
        for line in file:
            grades.append(float(line.strip()))
            n_grades += 1
    return sum(grades)/n_grades


print(print_stars_to_file(5))
