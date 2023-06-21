# Да се състави програма на Python за управление на аптека. За целта дефинирайте клас Medicine с полета: 
# med_id, med_name, manufacturer, price, quantity.
# В класа да се дефинирани методите:
# Display(self), който показва информация за лекарството.
# Search_by_name(self, name), който търси лекарството по име.
# Sale(self), който е за продажба на оределено количество от аддено лекарство.
# Purchase(self), който е за зареждане на нови количества от медикамента.
# Наличните лекарства в аптиката се съхраняват в списък med_list, като броя на тези медикаменти и необходимата информация
# за всеки медикамент се въвеждат от клавиатурата.
# Да се дефинира функция Sort_Meds(), която да сортира лекарствата по атрибута name.
# Да се дефинира функция minimal_quantity_from_manufacturer(manufacturer), която показва информация за лекарството с най-малка наличност от даден производител.

class Medicine:
    def __init__(self, med_id, med_name, manufacturer, price, quantity):
        self.med_id = med_id
        self.med_name = med_name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity

    def Display(self):
        print(f"{self.med_id} {self.med_name} {self.manufacturer} {self.price} {self.quantity} ")

    def __repr__(self):
        return (f"{self.med_id} {self.med_name} {self.manufacturer} {self.price} {self.quantity} ")

    def Search_by_name(self,name):
        for med in med_list:
            if med.med_name == name:
                return med.Display()

    def Sale(self):
        quantity = int(input("Enter quantity: "))
        self.quantity -= quantity

    def Purchase(self):
        quantity = int(input("Enter quantity: "))
        self.quantity += quantity

med_list = []
n = int(input("Enter number of medicaments: "))
for x in range(n):
    med_id = float(input("Enter med_id: "))
    med_name = input("Enter med_name: ")
    manufacturer = input("Enter manufacturer: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    med = Medicine(med_id, med_name, manufacturer, price, quantity)
    med_list.append(med)

def Sort_Meds(med_list):
    return sorted(med_list, key=lambda y:y.med_name, reverse=False)

def minimal_quantity_from_manifacturer(manifacturer):
    same_manifa = []
    for med in med_list:
        if med.manufacturer == manifacturer:
            same_manifa.append(med)
    small_quantity = same_manifa[0]
    for x in same_manifa:
        if x.quantity < small_quantity.quantity:
            small_quantity = x
    return small_quantity
