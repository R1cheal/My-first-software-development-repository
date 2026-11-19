student1={
  "name":"ABC",
  "course":"Python",
  "mark":90
}

print(student1["name"], student1["mark"]) #Print the student’s name and mark using their dictionary keys.

if student1["mark"]>=50: #If the mark is 50 or higher, print Pass; otherwise print Review required.
  print("Pass!")
else:
  print("Review required.")

student1["mark"]=65 #Update the mark, print the full record and observe what changed.
print(student1)

student2={
  "name":"BCD",
  "course":"Python",
  "mark":78
}
list=[student1, student2]
print(list) #Create a list containing two student dictionaries and display both.
