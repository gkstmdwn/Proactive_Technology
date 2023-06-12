import csv
import sys

from student import student
from study import study, Mentor_Mentee, Study_Group

class main():
    def __init__(self) -> None:
        self.student_dict = dict()
        # f = open('./Proactive Technology/student_data.csv', 'r', encoding='utf-8')
        f = open('./Proactive Technology/student_data_Gaussian.csv', 'r', encoding='utf-8')
        reader = csv.reader(f)
        for line in reader:
            name = line[1]
            grade_dict = {'국어': line[2], '영어': line[3], '수학': line[4], '사회': line[5], '과학': line[6]}
            temp_student = student(name, grade_dict)
            self.student_dict[name] = temp_student
        f.close()

    def __str__(self) -> str:
        return str(len(self.student_dict))+"명의 학생이 포함되어 있습니다."

    def available_student_list(self):
        available_student_list = []
        for i, value in self.student_dict.items():
            if value.is_available == True:
                available_student_list.append(value)
        return available_student_list

    def recommend_mentor(self, target_student:str, subject) -> list:
        target_student_grade = self.student_dict[target_student].grade[subject]
        mentor_list = []
        for student in self.student_dict.values():
            if student.grade[subject] > target_student_grade + 10:
                mentor_list.append(student)
        return mentor_list
    
    def recommend_mentee(self, target_student:str, subject) -> list:
        target_student_grade = self.student_dict[target_student].grade[subject]
        mentee_list = []
        for student in self.student_dict.values():
            if student.grade[subject] < target_student_grade + 10:
                mentee_list.append(student)
        return mentee_list

    def recommend_studygroup(self, target_student:str, subject) -> list:
        target_student_grade = self.student_dict[target_student].grade[subject]
        studygrouplist = []
        for student in self.student_dict.values():
            if (student.grade[subject] + 10 > target_student_grade) & (student.grade[subject] - 10 < target_student_grade):
                studygrouplist.append(student)
        return studygrouplist

    def make_studygroup(self, subject:str, *students:str):
        student_list = []
        for student_name in students:
            student_list.append(self.student_dict[student_name])
        print(student_list)
        New_Studygroup = Study_Group(subject, student_list)
        return New_Studygroup






if __name__ == "__main__":
    Study_Program = main()
    print(Study_Program)
    mentor=Study_Program.recommend_studygroup('student1', '사회')
    print(mentor)
    studygroup = Study_Program.make_studygroup('사회', 'student1', 'student2')
    print(studygroup.student_list)