#Concatenation of string
a="hello"
b="world"
c=a+" "+b       
print(c)
greetings= a+" is the starting , "+b+" !"
print('Concatenation : ', greetings)

#len is used to find the length of the string
print(len(c))   
print(len(greetings))



# #indexing of string
print("First character : ",c[0])   
print("Last character : ",c[-1])   #this will give us the last character of the string
                                   #we can only see char not modify in string because string is immutable



#  slicing of string [start : stop : step]
print("First five characters " , c[0:5])   
#  remember the 0 is starting index it is involved but the 5 the closing index is not closed so it will give us the characters from index 0 to 4

print("The Charcter from index 6 to 11 ", c[6:11])   
print("Whole string " , c[1:]) # because we have not given any closing index so it will give us the whole string


# negative indexing of string cannot reverse the string but we can access the characters from the end of the string using negative indexing
print("Last Character ", c[-1])    
print("Second Last Character ", c[-2])   
print(c[-1:-10])  #this will give us the characters from index -1 to -10 but it will not give us any character because the closing index is not involved and the starting index is greater than the closing index so it will give us an empty string
print("Character from 10 index from last to last char " , c[-10:-1])  #this will give us the characters from index -10



name = input("enter your name : ")
print(len(str(name)))  
str="Hassan is a good boy $$$$$$"
print("count():",str.count("$"))   #this will give us the count of $ in the string
print("upper():",str.upper())      # upper() - converts to uppercase
print("lower():",str.lower())      #lower() - converts to lowercase 

# strip() - removes leading and trailing whitespace
cleaned = str.strip()
print("strip():", f"{cleaned}")

#replace( old , new) -replace occurrences
print("replace()",cleaned.replace("Hassan","Meesum"))

username = print(f"{name}786_gamil.com ")
print("Username : " ,username)

# split(delimiter) - splits into a list (defaults to whitespace)
sentence = "apple,banana,cherry,orange"
fruits=sentence.split(",")
print("split()",fruits)


# Formatted strings (f-strings) - cleaner than concatenation

name = "hassan"
age = 45
print(f" My name is {name} and my age is {age}")

# Escape characters (\n for newline, \t for tab, \" for quote)
print("Line 1\n\tIndented Line 2 with \"quotes\"")

# Checking content (startswith, endswith, in)
print("Starts with 'P'?", cleaned.startswith("P"))  # True
print("Contains 'Prog'?", "Prog" in cleaned)