n=int(input("Enter a number:"))
l=[]
for i in range(n):
  if i%2==0 and i!=0:
    l.append(i)
print("Even numbers:", l)
print("Count:", len(l))
