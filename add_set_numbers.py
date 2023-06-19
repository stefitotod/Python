s = set()
for i in range(1, 51):
     if(i % 3 == 0 or i % 4 == 0) and i % 12 != 0:
          s.add(i)
print(s)
