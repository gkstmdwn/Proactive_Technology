from student import student

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

class Mentor_Mentee(study):
    pass

class Study_Group(study):
    pass

if __name__ == "__main__":
    student1 = student("한승주", {"국어": 100, "영어":100.0})
    student2 = student("한희나", {"국어": 80, "영어":90})
    
    study1 = study('국어', [student1, student2])
    print(study1.student_list)