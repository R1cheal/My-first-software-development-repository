subjects=["Python", "Security", "AI"]
print("Subject list:", subjects)
print("First and last subject:", subjects[0], subjects[len(subjects)-1]) #Print the first and last items in the list.
subj=input("Enter a subject:")
subjects.append(subj) #Ask the user for one more subject and add it using append().
for i in subjects: #Use a loop to print every subject on a separate line.
  print(i)
if "Python" in subjects:  #Check whether "Python" is present using the in operator.
  print("Yes! Python is in the subject list")
subjects.remove("AI")  # Remove one subject and print the updated list.
print("Updated list:", subjects)
