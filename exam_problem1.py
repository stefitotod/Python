# Напишете програма, в която потребителят въвежда две цели числа n и k.
# След това въвежда още толкова числа, колкото е стойността на n. Създайте два списъка.

# В първия списък да се добавят само тези числа, от въведените n на брой, които са по-големи от k.
# Да се намери произведението на елементите от този списък, чиито индекси са нечетни. Да се намери индекса на елемента с минимална стойност.

# Във втория списък да се добавят тези числа от въведените n на брой, които са по-малки или равни на k и са положителни.
# Да се намери разликата между елемента с максимална и елемента с минимална стойност.

while True:
    try:
        n = int(input("Enter integer n : "))
        if n <= 0:
            raise ArithmeticError("Enter a positive number.")
        break
    except ValueError:
        print("Enter integer.")
    except ArithmeticError as error:
        print(error)

while True:
    try:
        k = int(input("Enter integer k : "))
        if k <= 0:
            raise ArithmeticError("Enter a positive number.")
        break
    except ValueError:
        print("Enter integer.")
    except ArithmeticError as error:
        print(error)

list1 = []
list2 = []

x = 0
while x < n :
    num = int(input("Enter number: "))
    if num > k :
        list1.append(num)
    elif num <= k and num > 0:
        list2.append(num)
    x += 1

print(list1)
print(list2)

pr = 1
if len(list1) > 0:
    for i in range(1,len(list1),2):
        pr = pr*list1[i]
    min_num = list1.index(min(list1))
    print(pr)
    print(min_num)
else:
    print("list1 is empty !")

if len(list2) > 0:
    difference = max(list2) - min(list2)
    print(difference)
else:
    print("list2 is empty !")



