class Computer:
    # In class, we have:
    # attributes --> Variables
    # Behaviours --> Methods(Functions)
    def __init__(self, cpu, ram):
        print("we are in init")
        self.cpu = cpu
        self.ram = ram

    def Config(self):
        print("config is", self.cpu, self.ram)  # cpu belongs to object that's why we are using self.


comp1 = Computer('i5', 16)
comp2 = Computer('Ryzen', 8)

# a = '8'
# print(type(a)) #comes in string class.
# print((type(comp1))) #comes in Computer class.


# Computer.Config(comp1)
# Computer.Config(comp2)
comp1.Config()
comp2.Config()
