# Напишете програма, която ще реализира калкулатор за цели числа- събиране, изваждане, умножение и деление.
# Потребителят въвежда вида на операцията. След това въвежда две цели числа.
# Резултатът се принтира. Реализирайте отделни функции (за отделните операции).

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error"
    else:
        return x / y

print("Select operation!")
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide")

choice = input("Enter 1, 2, 3 or 4 : ")
if choice in (f"1,2,3,4"):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

if choice == '1':
    print(add(num1, num2))

elif choice == '2':
    print(subtract(num1, num2))

elif choice == '3':
    print(multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
