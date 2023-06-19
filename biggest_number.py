n = int(input("How many numbers do you have?\n"))
biggest_number = 0
for i in range (n):
  num = int(input("Enter a number: "))
  if num > biggest_number:
    biggest_number = num
print(biggest_number)
