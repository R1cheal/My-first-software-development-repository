password="python123"
i=0
while i<3:
  pwd=input("Enter password:")
  if pwd==password:
    print("Access granted!")
    break
  else:
    print(3-(i+1), "attempts remaining.")
    if i==2:
      print("Access denied!")
  i+=1
