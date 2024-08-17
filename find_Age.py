from datetime import date


class Person:

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def person_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(self.date_of_birth.month, self.date_of_birth.day):
            age = age - 1
        return age


P1 = Person("Sharath", date(1995, 3, 3))
P2 = Person("Sushmitha", date(1996, 9, 23))
print("Person 1", P1.name, P1.date_of_birth, P1.person_age())
print("Person 2", P2.name, P2.date_of_birth, P2.person_age())
