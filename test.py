class Employee:
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname (self):
        return f'{self.first} {self.last} is my name'

    def applyRaise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('Conor','Ladrigan',50000)
print(emp1.pay)
emp1.applyRaise()
print(emp1.pay)

print(Employee.__dict__)
