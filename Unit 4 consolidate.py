import csv
import os

file="inventory.csv"
fields = (Product_name, Quantity, Price_per_piece,)
rows = []   

with open(inventory.csv, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields) #add headings to columns

def add_product():
  n=input("Enter product name:")
  q=int(input("Enter quantity:"))
  r=float(input("Enter price per piece:"))
  list=[]
  list.append(n)
  list.append(q)
  list.append(r)
  with open(inventory.csv, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(list)


  
  
