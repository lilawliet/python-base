# -*- coding: utf-8 -*-
# __author__:HPW

class Student:
    def __init__(self, students) -> None:
        self.students = students

    # 魔法函数
    def __iter__(self):
        return iter(self.students)
    
    def __getitem__(self, index):
        return self.students[index]
    

student = Student(['a','b','c'])

student1 = student[:2]

print(student1)
print(type(student1))
print(len(student1))
# students = student.students

# for item in student:
#     print(item)