success = float(input("Enter success: "))
max_scholarship = float(input("Enter maximum scholarship: "))
if success >= 5.50:
  print(max_scholarship)
elif 5 <= success < 5.50:
  print(max_scholarship*0.7)
elif 4.50 <= success < 5:
  print(max_scholarship*0.5)
else:
  print("Sorry")
 
  
