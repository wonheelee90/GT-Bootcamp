def aslists(grades):
    grades_dict = {}
    for student in grades:
        grades_dict[student[0]] = [student[1], student[2], student[3]]
    del grades_dict['Student']
    return grades_dict

def asdicts(grades):
    grades_dict = {}
    for student in grades:
        grades_dict[student[0]] = {'Exam 1': student[1], 'Exam 2': student[2], 'Exam 3': student[3]}
    del grades_dict['Student']
    return grades_dict

import numpy as np
def stud_means(grades_dict):
    mean_dict = {}
    for student in grades_dict.keys():
        grade = grades_dict[student]
        avg_grade = np.mean(grade)
        mean_dict[student] = avg_grade
    return mean_dict