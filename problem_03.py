"""
Problem:
Create a class Student with:
    •    Private attribute: __marks
    •    Methods: set_marks(marks) and get_marks()

Demonstrate how encapsulation protects the data.
"""

class mark():
    
    def set_marks(marks,add_value):
        print (marks+add_value)
    def get_marks(marks):
        print(marks)

class student:
    def __init__(self,marks, add_value=0, sub_value = 0):
        self.marks=marks
