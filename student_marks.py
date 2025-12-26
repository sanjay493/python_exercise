class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
    
    def is_pass(self):
        return self.marks >= 40
    
    def grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 70:
            return 'B'
        elif self.marks >= 40:
            return 'C'
        else:
            return 'Fail'
    def display(self):
        print(f"Student Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Pass Status: {'Pass' if self.is_pass() else 'Fail'}")
        print(f"Grade: {self.grade()}")
