class Employee:
    def __init__(self, name, id, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print("ID : %d\nName : %s\nDepartment : %s\nSalary : %d" % (self.id, self.name, self.department, self.salary))


emp1 = Employee("Rohit", 264, "CE", 10000)
emp2 = Employee("Virat", 183, "IT", 20000)
emp3 = Employee("Dhoni", 183, "AI", 30000)

emp1.display()
print("\n")
emp2.display()
print("\n")
emp3.display()
