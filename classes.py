# Да се дефинира клас Person с полета име, фамилия, възраст, националност.
# Да се дефинира конструктор, който инициализира полетата на класа.
# Да се добави метод printinfo(), който отпечатва имената и националността.
# Създайте две инстанции на класа и за тях извикайте метод printinfo().

# Да се дефинира клас Student, който наследява класа Person.
# Той трябва да има още две полета - университет и година на обучение.
# Да се предефинира метода printinfo(), така че да се отпечатва и информацията от новите полета.
# Създайте две инстанции от класа Student и за тях извикайте метод printinfo().

class Person:

    def __init__(self, fname, lname, age, nationality):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.nationality = nationality

    def printinfo(self):
        print(f"{self.fname} {self.lname} ,  {self.nationality}")


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
