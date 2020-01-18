class Student:
    '''This is student class required data'''
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z

    def display(self):
        print("Student Name:{}\nrollno:{}".format(self.name,self.rollno,self.marks))

s=Student("surya",101,75)
s.display()
s1=Student("uday",102,99)
s1.display()