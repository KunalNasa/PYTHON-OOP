class Students:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(f"The name is {self.name} and the roll number is {self.rollno}")
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'Apple'
            self.cpu = 'M1'
            self.ram = 8

        def show(self):
            print(f"Brand name is {self.brand}, CPU is {self.cpu} and ram is {self.ram}GB.")


s1 = Students('Kunal', 15)
s2 = Students('Navin', 20)
s1.show()

# lap1 = Students.Laptop()

# lap1 = s1.lap
# lap2 = s2.lap
# print(id(lap1))
# print(id(lap2))