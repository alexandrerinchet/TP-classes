from students import Student
from collections import defaultdict

class Class:
    def __init__(self, classname: str):
        self.classname = classname
        #dico et pas liste
        self.students = {} 

    def add_student(self, student: Student):
        #j'utilise une clé pour stocker les élèves, vu que c'est un dico
        key = (student.first_name, student.last_name)
        self.students[key] = student

    def __len__(self):
        return len(self.students)

    def __repr__(self):
        return f"Class {self.classname} - {len(self.students)} student(s)"
    
    def get_student(self, first_name, last_name):
        key = (first_name, last_name)
        if key in self.students:
            return self.students[key]
        else:
            return None
        
    def load_students_from_file(self, filename: str):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) >= 2:
                        first_name = parts[0].strip()
                        last_name = parts[1].strip()
                        student = Student(first_name, last_name)
                        self.add_student(student)
    
    def load_grades_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = [p.strip() for p in line.split(',')]
                    if len(parts) >= 3:
                        first_name = parts[0]
                        last_name = parts[1]
                        topic = parts[2]
                        grades = [float(grade) for grade in parts[3:]]
                        
                        student = self.get_student(first_name, last_name)
                        if student:
                            for grade in grades:
                                student.add_grade(topic, grade)
    
    def catalog(self):
        catalog = defaultdict(int)
        for student in self.students.values():
            for topic in student.followed_topics():
                catalog[topic] += 1
        return dict(catalog)
    
    def compute_averages(self):
        # on va chercher à faire la moyenne des moyennes des élèves
        topic_sums = defaultdict(float)
        topic_counts = defaultdict(int)
        
        for student in self.students.values():
            for topic in student.followed_topics():
                avg = student.compute_average(topic)
                if avg != -1:
                    topic_sums[topic] += avg
                    topic_counts[topic] += 1
        
        class_averages = {}
        for topic in topic_sums:
            if topic_counts[topic] > 0:
                class_averages[topic] = topic_sums[topic] / topic_counts[topic]
                
        return class_averages






    






  