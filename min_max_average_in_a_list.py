l = []
length = int(input("Enter length: "))
for i in range(length):
    num = int(input("Enter a number: "))
    l.append(num)
print(f"min: {min(l)}, max: {max(l)}, average: {sum(l)/len(l)}")

