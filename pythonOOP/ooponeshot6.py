# DUCK TYPING-----
"""
class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()


#ide = PyCharm()
ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)
"""


# OPERATOR OVERLOADING------
# a = '5'
# b = '6'
# # print(int.__add__(a,b))
# print(str.__add__(a, b))
# print(a + b)


class Students:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        addition = Students(m1, m2)
        return addition

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        subtract = Students(m1, m2)
        return subtract

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{},{}'.format(self.m1, self.m2)


s1 = Students(40, 60)
s2 = Students(50, 100)

addition = s1 + s2
subtract = s1 - s2
print(addition.m1)  # 40+50
print(subtract.m2)

if s1 > s2:
    print("s1 is greater")
else:
    print("s2 is greater")

print(s1)
