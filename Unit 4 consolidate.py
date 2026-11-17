import csv
import os

file="inventory.csv"
fields = (Product_name, Quantity, Price_per_piece,)

def create_header():
    with open(file, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields) #add headings to columns

def add_product(): #
    n=input("Enter product name:")
    q=int(input("Enter quantity:"))
    r=float(input("Enter price per piece:"))
    list=[]
    list.append(n)
    list.append(q)
    list.append(r)
    with open(file, 'a', newline=" ") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(list)
    print("Product added!")

def search_product():
    n=input("Enter product name:")
    record=[]
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)  #skip the headings
        for row in csvreader:
            if n.lower() == row[0].lower():
                record=row
                print("Product_name:", row[0], "\nQuantity", row[1], "\nPrice_per_piece", row[2])
                break
    if record==[]:
        print("Product not in inventory.")

def list_inventory():
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader) 
        print(header)   
        for row in csvreader: 
            print(row,"\n") 
        print("Total number of products: %d" % csvreader.line_num)
    
def update_product():
    n=input("Enter the product you would like to update:")
    rows=[]
    with open(file, 'r') as csvfile:
        csvreader=csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    for i in rows:
        if n in i:
            continue
        else:
            print("Product not in inventory.")
            return
    f=input("Enter the field you would like to update:")
    if f.lower()=="product_name":
        name_new=input("Enter the new product name:")
        updated_row=[]
        with open(file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if n.lower() == row[0].lower():
                    quantity=row[1]
                    price=row[2]
                    updated_row.append(name_new)
                    updated_row.append(quantity)
                    updated_row.append(price)
                    break
    elif f.lower()=="quantity":
        quantity_new=input("Enter the new quantity:")
        updated_row=[]
        with open(file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if n.lower() == row[0].lower():
                    name=row[0]
                    price=row[2]
                    updated_row.append(name)
                    updated_row.append(quantity_new)
                    updated_row.append(price)
                    break
    elif f.lower()=="price_per_piece":
        price_new=input("Enter the new quantity:")
        updated_row=[]
        with open(file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if n.lower() == row[0].lower():
                    name=row[0]
                    quantity=row[1]
                    updated_row.append(name)
                    updated_row.append(quantity)
                    updated_row.append(price_new)
                    break
    else:
        print("Invalid field entered.")
        return
    with open(file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter = csv.writer(csvfile)
        for row in rows:
            if n.lower()==row[0].lower():
                csvwriter.writerow(updated_row)
            else:
                csvwriter.writerow(row)
    print("Inventory updated!")

def remove_product():
    n=input("Enter product you want to remove:")
    rows=[]
    with open(file, 'r') as csvfile:
        csvreader=csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    for i in rows:
        if n in i:
            continue
        else:
            print("Product not in inventory.")
            return
    with open(file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in rows:
            if n.lower()==row[0].lower():
                continue
            else:
                csvwriter.writerow(row)
    print("Record deleted!")
