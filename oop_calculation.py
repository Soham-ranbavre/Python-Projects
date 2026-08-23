# Day 15 - Python OOP: Methods with Calculations

class Student:

    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def calculate_percentage(self):
        total = self.marks1 + self.marks2 + self.marks3
        percentage = total / 3
        return percentage

    def display_result(self):
        print("Name:", self.name)
        print("Percentage:", self.calculate_percentage())


student1 = Student("Student1", 80, 75, 90)

student1.display_result()
