# Програмата дава възможност на потребителя да въвежда неограничен брой цели числа.
# Да се даде процентът на числата, кратни на седем, резултатът да се закръгли до втория знак след десетичната запетая.
# Да се изведе сумата на числата, които не са кратни на седем.
# Да се изведе максималното число.
# Да се намери средноаритметичното на числата, кратни на седем, закръглени до третата цифра.

my_list1 = []

while True:
    try:
        num = int(input("Enter a number: "))
        my_list1.append(num)

    except ValueError:
        break

sevens = []
not_sevens = []

for x in my_list1:
    if x % 7 == 0:
        sevens.append(x)
    else:
        not_sevens.append(x)

print(f"{len(sevens)/len(my_list1):.2%}")
print(f"{sum(not_sevens)}")
print(f"{max(my_list1)}")
print(f"{sum(sevens)/len(sevens):.3f}")
