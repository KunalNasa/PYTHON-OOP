# To format document - option + command + Shift + L
"""
class A:
    def feature1(self):
        print("Feature1 working.")
    def feature2(self):
        print("Feature2 working.")

# class B(A):
class B:
    def feature3(self):
        print("Feature3 working.")
    def feature4(self):
        print("Feature4 working.")
# class C(B):
class C(A,B):
    def feature5(self):
        print("Feature5 working.")

a1 = A()
b1 = B()
c1 = C()
a1.feature1()
# b1.feature1() #inherited feature from class A.
c1.feature1() #inherited feature from class B which is further inherited from class A.
"""


# Subclass can access all the features of Superclass but converse is not true.
# CONSTRUCTOR IN INHERITANCE..........
class A:
    def __init__(self):
        print("In A init.")

    def feature1(self):
        print("Feature1-A working.")

    def feature2(self):
        print("Feature2 working.")


#class B(A):
class B:
    # If you create object of Sub class it will first try to find init of Sub class
    # if it is not found then it will call init of Super class.
    def __init__(self):
        # super().__init__()
        print("In B init.")

    def feature1(self):
        print("Feature1-B working")

    def feature3(self):
        print("Feature3 working.")

    def feature4(self):
        print("Feature4 working.")

class C(A,B):
    def __init__(self):
        super().__init__() #Find init of first class in Bracket(Here it is A).
        print("In C init.")
#a1 = B()
a1 = C()
a1.feature1() #calls the feature of left class in bracket(or you can say first class in bracket).


#POLYMORPHISM-------
#four ways of Polymorphism.
#1. Duck Typing
#2. Operator Overloading
#3. Method Overloading
#4. Method Overriding

x = 5
x = 'Navin'
print(type(x))