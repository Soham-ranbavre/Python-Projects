# Day 13 - Python OOP Basics

class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def introduce(self):
        print("My name is", self.name)
        print("My age is", self.age)
        print("My branch is", self.branch)


student1 = Student("Student", 21, "AIML")

student1.introduce()
