import sys
import csv

class student():
    def __init__(self, name:str, grade:dict) -> None:
        self.name = name
        self.grade = grade
        self.is_available = True
        for key, value in self.grade.items():
            self.grade[key] = float(value)

    def __str__(self) -> str:
        return "이름:{name}, 성적:{grade}".format(name=self.name, grade=self.grade)
    
    def __repr__(self) -> str:
        return self.name
    
    def update_grade(self, grade:dict) -> None:
        self.grade = grade
        for key, value in self.grade.items():
            self.grade[key] = float(value)

class study():
    def __init__(self, subject:str, *students:student) -> None:
        if type(students[0]) == list:
            self.student_list = students[0]
        elif type(students[0]) == student:
            self.student_list = []
            for std in students:
                self.student_list.append(std)
        self.subject = subject

    def __str__(self) -> str:
        return str(self.student_list)

class main():
    def __init__(self) -> None:
        self.student_dict = dict()
        f = open('./student_data_Gaussian.csv', 'r', encoding='utf-8')
        reader = csv.reader(f)
        for line in reader:
            name = line[1]
            grade_dict = {'국어': line[2], '영어': line[3], '수학': line[4], '사회': line[5], '과학': line[6]}
            temp_student = student(name, grade_dict)
            self.student_dict[name] = temp_student
        f.close()
        self.grade_average = {}

    def __str__(self) -> str:
        return str(len(self.student_dict))+"명의 학생이 포함되어 있습니다."

    def __len__(self) -> str:
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
        New_Studygroup = study(subject, student_list)
        return New_Studygroup

if __name__ == "__main__":
    Study_Program = main()
    print(Study_Program)
    mentor=Study_Program.recommend_studygroup('student1', '사회')
    print(mentor)
    studygroup = Study_Program.make_studygroup('사회', 'student1', 'student2')
    print(studygroup.student_list)