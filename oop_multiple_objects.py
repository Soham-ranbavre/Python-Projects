# Day 14 - Python OOP: Multiple Objects

class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)
        print()


student1 = Student("Student1", 21, "AIML")
student2 = Student("Student2", 22, "CSE")

student1.introduce()
student2.introduce()
