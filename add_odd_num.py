# Напишете програма с функция, която получава като аргумент числов списък.
# Връща като резултат друг списък, в който са включени само нечетните числа от списъка аргумент.

def add_odd_num(list1):
  list2 = []
  for x in list1:
      if x % 2 == 0:
          pass
      else:
          list2.append(x)
  return list2

print(add_odd_num([1, 2, 3, 4, 5]))
        
