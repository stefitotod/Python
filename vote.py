# Потребителят въвежда възраст.
# На екрана се принтира съобщение: имаш право да гласуваш или не.

while True:
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            raise ArithmeticError("Enter a positive number.")
    except ValueError:
        print("Enter integer.")
    except ArithmeticError as err:  
        print(err)
    else:
         if num >= 18 and num < 100:
            print("You can vote.")
         else:
             print("You can't vote.")
         break
