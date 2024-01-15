#Types of variables in OOP-
#1.Instance Variable
#2.Class(Static) Variable
#variables inside init are instance variables.
#variables outside init but inside a class are class variables.

#Types of methods:
#1.Instance methods
#2.Class methods
#3.Static methods

#In Instance, we have different types.
#1.Accessors method
#2.Mutators method
"""
class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "Mercedes"

c1 = Car()
c2 = Car()

c1.mil = 12
print(c1.com, c1.mil)
print(c2.com, c2.mil)
"""

class Students:

    school = "Kannu ka skool"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class...in abc module")

s1 = Students(20,30,40)
s2 = Students(40,50,44)

print(s2.average())
print(Students.getschool())
s1.info()