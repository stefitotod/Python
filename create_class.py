# Да се дефинира клас Person с полета име, фамилия, възраст, националност.
# Да се дефинира конструктор, който инициализира полетата на класа.
# Да се добави метод printinfo(), който отпечатва имената и националността.
# Създайте две инстанции на класа и за тях извикайте метод printinfo().

class Person:

    def __init__(self, fname, lname, age, nationality):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.nationality = nationality

    def printname(self):
        print(f"{self.fname} {self.lname} , {self.nationality}")


Yoana = Person("Yoana", "Qnkova", 19, "bulgarian") 
Vasko = Person("Vasko", "Uzunov", 20, "bulgarian")

Yoana.printname()
Vasko.printname()
