# Създава се списък от 20 елемента с повтарящи се такива. Да се създаде нов списък на базата на първия, но само с уникални елементи.

list34 = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7]
new_list = []
for x in list34:
    if x not in new_list:
        new_list.append(x)
    else:
        pass
print(new_list)
