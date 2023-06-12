class student():
    def __init__(self, name:str, grade:dict) -> None:
        """ class for managing students
        Args:
            name (str): Name of the student
            grade (dict): Grade Dictionary of the student, key should be subject name(str), value should be score(float)
        """
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
        """ function for updating student's grade

        Args:
            grade (dict): _description_
        """
        self.grade = grade
        for key, value in self.grade.items():
            self.grade[key] = float(value)





if __name__ == "__main__":
    student1 = student("한승주", {"국어": 98, "영어":100.0})
    print(student1)