import sys
import csv
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit
import Study

class STUDY():
    def __init__(self):
        self.student_dict = dict()
        f = open("./student_data_Gaussian.csv", 'r', encoding='utf-8')
        reader = csv.reader(f)
        g1, g2, g3, g4, g5 = [], [], [], [], []
        for line in reader:
            name = line[1]
            grade_dict = {'국어': float(line[2]),
                          '영어': float(line[3]), '수학': float(line[4]),
                          '사회': float(line[5]), '과학': float(line[6])}
            temp_student = Study.student(name, grade_dict)
            self.student_dict[name] = temp_student
            g1.append(float(line[2]))
            g2.append(float(line[3]))
            g3.append(float(line[4]))
            g4.append(float(line[5]))
            g5.append(float(line[6]))
        f.close()
        self.grade_avg = {'국어': np.average(g1),
                          '영어': np.average(g2), '수학': np.average(g3),
                          '사회': np.average(g4), '과학': np.average(g5)}
        self.grade_stdev = {'국어': np.std(g1),
                          '영어': np.std(g2), '수학': np.std(g3), 
                          '사회': np.std(g4), '과학': np.std(g5)}

    def recommend_mentor(self, target_student:str, subject) -> list:
        target_student_grade = self.student_dict[target_student].grade[subject]
        mentor_list = []
        for student in self.student_dict.values():
            if student.grade[subject] > target_student_grade + self.grade_stdev[subject]:
                mentor_list.append(student)
        return str(mentor_list)

    def recommend_mentee(self, target_student:str, subject) -> list:
        target_student_grade = self.student_dict[target_student].grade[subject]
        mentor_list = []
        for student in self.student_dict.values():
            if student.grade[subject] < target_student_grade - self.grade_stdev[subject]:
                mentor_list.append(student)
        return str(mentor_list)

    def recommend_study_group(self, target_student:str, subject) -> list:
        target_student_grade = self.student_dict[target_student].grade[subject]
        mentor_list = []
        for student in self.student_dict.values():
            if student.grade[subject] > target_student_grade - self.grade_stdev[subject] and student.grade[subject] < target_student_grade + self.grade_stdev[subject]:
                mentor_list.append(student)
        return str(mentor_list)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.Study_Program = STUDY()
        self.initUI()

    def initUI(self):
        # GUI의 설정을 합니다.
        self.setWindowTitle('Recommender')

        # Vertical layout을 설정합니다.
        layout = QVBoxLayout()

        # 이름을 입력받을 위젯을 생성합니다.
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter Name")

        # 과목명을 입력받을 위젯을 생성합니다.
        self.subject_input = QLineEdit()
        self.subject_input.setPlaceholderText("Enter Subject")

        # Button을 생성하고 누르면 recommend_mentor 함수의 결과를 라벨에 보여줍니다.
        self.mentor_button = QPushButton('Recommend a Mentor', self)
        self.mentor_button.clicked.connect(self.on_mentor_click)

        # Button을 생성하고 누르면 recommend_mentee 함수의 결과를 라벨에 보여줍니다.
        self.mentee_button = QPushButton('Recommend a Mentee', self)
        self.mentee_button.clicked.connect(self.on_mentee_click)

        # Button을 생성하고 누르면 recommend_study_group 함수의 결과를 라벨에 보여줍니다.
        self.study_group_button = QPushButton('Recommend a Study Group', self)
        self.study_group_button.clicked.connect(self.on_study_group_click)

        # 결과를 보여줄 라벨을 생성합니다.
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        # 레이아웃에 위젯을 추가합니다.
        layout.addWidget(self.name_input)
        layout.addWidget(self.subject_input)
        layout.addWidget(self.mentor_button)
        layout.addWidget(self.mentee_button)
        layout.addWidget(self.study_group_button)
        layout.addWidget(self.text_edit)

        self.setLayout(layout)

    def on_mentor_click(self):
        # 버튼을 누르면 recommend_mentor 함수의 결과를 라벨에 보여줍니다.
        name = self.name_input.text()
        subject = self.subject_input.text()

        recommendation = self.Study_Program.recommend_mentor(name, subject)
        self.text_edit.setText(recommendation)

    def on_mentee_click(self):
        # 버튼을 누르면 recommend_mentee 함수의 결과를 라벨에 보여줍니다.
        name = self.name_input.text()
        subject = self.subject_input.text()

        recommendation = self.Study_Program.recommend_mentee(name, subject)
        self.text_edit.setText(recommendation)

    def on_study_group_click(self):
        # 버튼을 누르면 recommend_study_group 함수의 결과를 라벨에 보여줍니다.
        name = self.name_input.text()
        subject = self.subject_input.text()

        recommendation = self.Study_Program.recommend_study_group(name, subject)
        self.text_edit.setText(recommendation)


def main():
    app = QApplication([])

    ex = MyApp()
    ex.show()

    app.exec_()

if __name__ == '__main__':
    main()