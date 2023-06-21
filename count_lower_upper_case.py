# Напишете програма, при която потребителят въвежда низ, а програмата извежда броят на главните и броят на малките букви.

word = input("Enter string:")
count1 = 0
count2 = 0
for i in word:
    if (i.islower()) :
        count1+=1
    elif (i.isupper()) :
        count2 += 1

print(f"The number of lowercase characters is: {count1}")

print(f"The number of uppercase characters is: {count2}")
