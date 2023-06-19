n = int(input("How many numbers do you have?\n"))
total = 0
while n > 0:
  num = int(input("Enter a number: "))
  total += num
  n -= 1
print(total)
