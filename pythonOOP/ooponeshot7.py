class Students:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def average(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            return (a + b + c) / 3
        elif a != None and b != None:
            return (a + b) / 2
        else:
            return a


s1 = Students(10, 20)
s2 = Students(30, 40)
print(s1.average(1, 2, 3))


# METHOD OVERRIDING-----
class A:
    def show(self):
        print("In A show")


class B(A):
    def show(self):
        print("In B show")


a1 = A()
b1 = B()
b1.show()
