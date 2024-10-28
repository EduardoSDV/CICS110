# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477

def get_names(x, y):
    name_and_surname = []
    for names in x:
        for names2 in y:
            name_and_surname.append(names+' '+names2)
    return name_and_surname

def average_scores(scores):
    penalty_percentages = {0: 1, 1: 0.9, 2: 0.75, 3: 0.5, 4: 0}
    return [sum(grade * (penalty_percentages[lateness] if lateness < 4 else 0) for grade, lateness in student) / len(student) for student in scores]






