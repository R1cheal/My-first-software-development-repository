temp=float(input("Enter the temperature:"))
if temp<10:
  print("Result: Cold")
  if temp<0:
    print("Freezing!")
elif temp<25:
  print("Result: Mild")
else:
  print("Result: Warm")
