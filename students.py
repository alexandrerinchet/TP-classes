from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str, grades: dict = None) :
        if grades is None :
            self.grades={}
        else :
            self.grades=grades
        self.first_name=first_name
        self.last_name=last_name

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    
    def add_grade(self, topic : str, grade : float) :
        if not (0<=grade<=20) :
            raise ValueError("Grade must be between 0 and 20.")
        self.grades[topic]=grade

    def followed_topics(self) :
        return list(self.grades.keys())
    
try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    topics = student.followed_topics()
    if len(topics) != 1 or "History" not in topics:
        raise Exception(f"Expecting ['History'] got {topics}")
except Exception as e:
    print('OOPS - There is an issue in your followed_topics method')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')