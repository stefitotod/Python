# Да се създаде списък с пет обекта от класа Lector.
# Да се дефинира функция, която получава като аргумент този списък и връща като резултат
# обекта с най-дълъг преподавателски опит.

class Person:

    def __init__(self, fname, lname, age, nationality):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.nationality = nationality

    def printinfo(self):
        print(f"{self.fname} {self.lname} , {self.nationality}")


Yoana = Person("Yoana", "Qnkova", 19, "bulgarian") 
Vasko = Person("Vasko", "Uzunov", 20, "bulgarian")

Yoana.printinfo()
Vasko.printinfo()

class Lector(Person):

    def __init__(self, fname, lname, age, nationality, unii, experience):
        Person.__init__(self, fname, lname, age, nationality)
        self.unii = unii
        self.experience = experience

    def printinfo(self):
        print(f"{self.fname} {self.lname} {self.age} {self.nationality} {self.unii} {self.experience}")

Lector1 = Lector("Ivana", "Ivanova", 45, "bulgarian", "TU", 8)
Lector2 = Lector("Petar", "Petrov", 67, "german", "UNSS", 34)

Lector1.printinfo()
Lector2.printinfo()


def the_best(lectors):
    result = lectors[0]
    for lector in lectors:
        if lector.experience > result.experience:
            result = lector
    return result

Pepi = Lector("Pepi", "Petrov", 80, "Turkey", "TU", 56)
Vankata = Lector("Vankata", "Ivanov", 45, "USA", "UNSS",5)

the_best([Pepi, Vankata]).printinfo()



