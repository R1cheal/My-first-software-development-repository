import csv
import os

file="inventory.csv"
fields = (Product_name, Quantity, Price_per_piece,)

with open(file, 'w') as csvfile: 
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
    with open(file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(list)
    print("Product added!")

def search_product():
    n=input("Enter product name:")
    with open(inventory.csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)  #skip the headings
    for row in csvreader:
        if n.lower() == row[0].lower():
            print("Product_name:", row[0], "\nQuantity", row[1], "\nPrice_per_piece", row[2])
        else:
            print("Product not in inventory.")

def list_inventory():
    with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    rows=[]
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total number of products: %d" % csvreader.line_num)
    print(rows)
    

def update_product():
    

            
        

  
