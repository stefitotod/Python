# Да се дефинира клас Person с полета име, фамилия, възраст, националност.
# Да се дефинира конструктор, който инициализира полетата на класа.
# Да се добави метод printinfo(), който отпечатва имената и националността.
# Създайте две инстанции на класа и за тях извикайте метод printinfo().

# Да се дефинира клас Student, който наследява класа Person.
# Той трябва да има още две полета - университет и година на обучение.
# Да се предефинира метода printinfo(), така че да се отпечатва и информацията от новите полета.
# Създайте две инстанции от класа Student и за тях извикайте метод printinfo().

# Да се добави към предходните задачи клас Lector, наследник на класа Person, с две нови
# полета - университет и опит.
# Да се предефинира метода printinfo(), така че да отпечатва новите полета.
# Да се създадат две инстанции и да се извика метода printinfo() за тях.

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

class Student(Person):

    def __init__(self, fname, lname, age, nationality, uni, year_uni):
        Person.__init__(self, fname, lname, age, nationality)
        self.uni = uni
        self.year_uni = year_uni

    def printinfo(self):
        print(f"{self.fname} {self.lname} {self.age} {self.nationality} {self.uni} {self.year_uni}")

Stefi = Student("Stefi", "Todorova", 19, "bulgarian", "TU", 2022)
Stefi.printinfo()

Ivayla = Student("Ivi", "Arnaudova", 23, "bulgarian", "UNSS", 2019)
Ivayla.printinfo()

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
