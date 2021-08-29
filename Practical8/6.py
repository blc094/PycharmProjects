class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class SportPerson(Person):
    def __init__(self, name, age, sport_name):
        Person.__init__(self, name, age)
        self.sport = sport_name

    def show(self):
        print("Name: ", self.name, "\nAge: ", self.age, "\nSport: ", self.sport)

s = SportPerson("BHANWAR LAL CHOUDHARY", 20, "Vollyeball")
s.show()