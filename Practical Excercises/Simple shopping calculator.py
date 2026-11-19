n=int(input("Enter the number of products you want to buy:"))
total=0
for i in range(n):
  product=input("Enter product name:")
  price=float(input("Enter price:"))
  quantity=int(input("Enter quantity:"))
  if price<=0 or quantity<=0:
    print("Error: You have entered a invalid price or quantity. Restart.")
    break
  else:
    total=total+price*quantity
print("Original total:", round(total,2), "GBP")
if total>50:
  print("Amount to pay:", round(total-total*0.1), "GBP")

  
  
  
