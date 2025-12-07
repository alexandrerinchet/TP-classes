from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str, grades: dict = None) :
        self.first_name = first_name
        self.last_name = last_name
        self.grades = {}

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    
    def add_grade(self, topic : str, grade : float) :
        if topic not in self.grades:
            self.grades[topic] = []
        self.grades[topic].append(grade)

    def followed_topics(self) :
        return list(self.grades.keys())
    
    def compute_average(self, topic: str):
        if topic not in self.grades:
            return -1.0
        
        notes_list = self.grades[topic]

        total = sum(notes_list)
        number_of_grades = len(notes_list)
        
        if number_of_grades == 0:
            return 0.0
            
        return total / number_of_grades
    
    def report(self):
        lines = []
        lines.append(f"Report for student {self.first_name} {self.last_name}")
        lines.append("+===============+===============+")
        lines.append("|     Topic     |    Average    |")
        lines.append("+===============+===============+")
        
        for topic in self.grades:
            average_val = self.compute_average(topic)
            
            line = f"|{topic:^15}|{average_val:^15.2f}|" #pour centrer le texte
            lines.append(line)
            lines.append("+---------------+---------------+")
            
        return "\n".join(lines)
    


