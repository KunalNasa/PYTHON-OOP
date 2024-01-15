# A constructor is a unique function that gets called automatically when an object is created of a class.
class Computer:
    def __init__(self):
        self.name = 'Kunal'
        self.age = 19

    def update(self):
        self.age = 28

    def compare(self,other):
        #c1 is self and c2 is other.
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer() #computer() is a constructor here.It calls the init method for us.
c2 = Computer()

print(id(c1)) #returns address of the memory.
print(id(c2))

c1.name = "Kannu" #changing name of c1.
print(c1.name)
c1.update() #self is assigning c1 to update.
print(c1.age)


c2.age = 12

if c1.compare(c2):
    print("They are same.")
else:
    print("They are different.")
