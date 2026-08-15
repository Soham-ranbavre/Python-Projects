# Day 8 - Python Dictionary

student = {
    "name": "Student",
    "age": 21,
    "branch": "AIML",
    "cgpa": 7.5
}

print("Student Name:", student["name"])
print("Branch:", student["branch"])
print("CGPA:", student["cgpa"])

student["cgpa"] = 7.8
student["city"] = "Pune"

print("\nUpdated Student Details:")
print(student)
