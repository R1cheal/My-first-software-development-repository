with open(sample_text.txt, 'r') as f:
  text=f.read()
  
text=text.lower()   #preparing the text for counting
text=text.split()
for i in range(len(text)):
	text[i]=text[i].strip(".")
	text[i]=text[i].strip(",")
  
word_dict={}  #creating the dictionary
for word in text:
  if word in word_dict.keys():
    word_dict[word]+=1
    continue
  else:
    word_dict[word]=1

print("Total words:", len(text))
print("Unique words:", len(word_dict))
print("WORDS AND THEIR FREQUENCIES:")
for word in word_dict:
  print(word,":",word_dict[word])
  
