# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:26:37 2021

@author: SST-Lab
"""

class Student:
     studentLevel = 'first year computer science 2020/2021 session'
     studentCounter = 0
     registeredCourse = 'CSC 102'
     def __init__(self, thename, thematricno, thesex, thehostelname, theage, thecsc102examscore):
         self.name = thename
         self.matricno = thematricno
         self.sex = thesex
         self.hostelname = thehostelname
         self.age = theage
         self.csc102examscore = thecsc102examscore
         Student.studentCounter = Student.studentCounter
         
     def age_checker(self):
         if self.age > '16':
             return self.age
         else:
             print ("student is not above 16")
             
     def examscore(self):
         if self.csc102examscore < '45':
             print ("you have to enroll for this course next year")
         else:
             return self.csc102examscore
             
     def getName(self):
         return  self.name

     def setName(self, thenewName):
         self.name = thenewName
         
     @classmethod
     def Register(cls):
         print("Registered course is " + cls.registeredCourse)

     @staticmethod
     def PAUNanthem():
        print('Pau, here we come, Pau, here we come ')
        
     @staticmethod
     def number(x):
         if x%2 == 0:
             print ("number is even")
         else:
             print ("number is odd")

student1 = Student('James Kaka', '021074', 'M', 'Amethyst', '20', '40')
print(studendt1.getName())
print(student1.examscore())

studendt1.setName('James Gaga')
print(studendt1.getName())

Student.PAUNanthem()

student1 = Student('David', '20120612107', 'Male', 'Cooperative', '19', '80')
print(student1.age_checker())
print(student1.examscore())

Student.Register()

Student.number(x = int(input("enter a number")))