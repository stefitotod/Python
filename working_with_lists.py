# Напишете програма, в която се създава фунцкия с два аргумента, явяващи се числови списъци.
# Резултатът от функцията се явява число, равно на сумата от двойките произведения на елементите на списъците.
# Ако в единия от списъците елементите са по-малко от другия, то недостигащите елементи се получават
# посредством циклично повторение на съдържанието на списъка.

list1 = [1, 2, 3]
list2 = [1, 2, 3, 1]

def my_function(list1, list2):
    a = 0
    if len(list1) >= len(list2):
        longer = list1
        shorter = list2
    else:
        longer = list2
        shorter = list1
    
    while len(shorter) < len(longer):
        shorter.extend(shorter)
    
    for x in range(len(longer)):
        a += longer[x]*shorter[x]
    
    return a

print(my_function(list1, list2))
