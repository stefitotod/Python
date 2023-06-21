# Напишете програма, в която се създава числов списък с n на брой елементи, като n се въвежда от потребителя и n е цяло число между 30 и 100 (30 < n < 100).
# Да се провери входа (дали условието "30 < n < 100" е изпълнено). 
# Списъкът се запълва със случайни числа в интервала от 20 до 600. Да се намери броят ва елементите от списъка, чиято цифла на едениците е кратна на 2.
# Да се намери индекса на минималния елемент от този списък, който има остатък 3 при целочислено деление на 7.

# Да се създаде 2 списък като се използва list comprehension и в него да се добавят тези числа от първия списък, които имат цифра на стотиците 3 или цифра на десетиците 5.
# Да се намери индекса на елемента с масимална стойност. Да се наемри произведението на елементите от списъка с цифра на единицете 3.

import random
while True:
    try:
        n = int(input("Enter n: "))
        if n > 30 and n < 100:
            break
        else:
            raise ArithmeticError("Please enter: n > 30 or n < 100!")
    except ValueError:
        print("Enter integer!")
    except ArithmeticError as error:
        print(error)

list1 = []
for x in range(n):
    list1.append(random.randint(20,600))
print(list1)

number = 0
for x in list1:
    if x % 2 == 0:
        number += 1
print(number)

list2 = []
for x in list1:
    if x % 7 == 3:
        list2.append(x)
print(list2)

if len(list2) > 0:
    min_num = list2.index(min(list2))
    print(min_num)
else:
    print("Sorry, list2 is empty")

second_list = [x for x in list1 if ( x // 100 == 3 or x // 10 % 10 == 5)]
print(second_list)

max_num_index = second_list.index(max(second_list))
print(max_num_index)

multi = 1
for x in second_list:
    if x % 10 == 3:
        multi *= x
print(multi)
