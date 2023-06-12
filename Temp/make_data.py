import csv
import random
import numpy as np
import matplotlib.pyplot as plt

def make_data():
    file = open('./Proactive Technology/student_data.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(file)
    for i in range(300):
        name = "student{}".format(str(int(i+1)))
        writer.writerow([i, name, round(random.uniform(0.0, 100.0), 1), round(random.uniform(0.0, 100.0), 1),
                        round(random.uniform(0.0, 100.0), 1), round(random.uniform(0.0, 100.0), 1), round(random.uniform(0.0, 100.0), 1)])



    file = open("./Proactive Technology/student_data_Gaussian.csv", 'w', encoding='utf-8', newline='')
    writer = csv.writer(file)

def make_gaussian_data():
    Language_Grades = []
    English_Grades = []
    Math_Grades = []
    SocialStudies_Grades = []
    Science_Grades = []

    while len(Language_Grades) != 300:
        mean, standard_deviation = 60, 15
        score = np.random.normal(mean, standard_deviation)
        if (score <= 100) and (score >= 0):
            Language_Grades.append(round(score, 1))

    while len(English_Grades) != 300:
        mean, standard_deviation = 70, 10
        score = np.random.normal(mean, standard_deviation)
        if (score <= 100) and (score >= 0):
            English_Grades.append(round(score, 1))
            
    while len(Math_Grades) != 300:
        mean, standard_deviation = 55, 17
        score = np.random.normal(mean, standard_deviation)
        if (score <= 100) and (score >= 0):
            Math_Grades.append(round(score, 1))

    while len(SocialStudies_Grades) != 300:
        mean, standard_deviation = 75, 13
        score = np.random.normal(mean, standard_deviation)
        if (score <= 100) and (score >= 0):
            SocialStudies_Grades.append(round(score, 1))

    while len(Science_Grades) != 300:
        mean, standard_deviation = 65, 17
        score = np.random.normal(mean, standard_deviation)
        if (score <= 100) and (score >= 0):
            Science_Grades.append(round(score, 1))

    file = open("./Proactive Technology/student_data_Gaussian.csv", 'w', encoding='utf-8', newline='')
    writer = csv.writer(file)

    for i in range(300):
        name = 'student{}'.format(str(int(i+1)))
        writer.writerow([i, name, Language_Grades[i], English_Grades[i], Math_Grades[i], SocialStudies_Grades[i], Science_Grades[i]])