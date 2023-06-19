# На функция се подават 2 аргумента- списък с числа и число.
# Променете всички елементи от списъка със стойност по-голяма от стойността на даденото число на нула.
# Функцията връща променения списък.

list1 = [1, 23, 5, 90]
num = 89

def changeelements(list1, num):
    for x in range(len(list1)):
        if list1[x] > num:
            list1[x] = 0
    return list1
  
print(changeelements(list1, num))
