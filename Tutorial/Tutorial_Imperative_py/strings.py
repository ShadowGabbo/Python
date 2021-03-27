#looping in a string 
for x in "banana":
  print(x)

#strign length 
a = "Hello, World!"
print(len(a))

#search a strign into another 
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#if there isnt in the string 
txt = "The best things in life are free!"
print("expensive" not in txt)

#slicing 
b = "Hello, World!"
print(b[2:5])

#slice from teh start 
b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

#negative indexing 
b = "Hello, World!"
print(b[-5:-2])

#to upper case
a = "Hello, World!"
print(a.upper())

#to bottom case 
a = "Hello, World!"
print(a.lower())

#remove white spaces 
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#replace string
a = "Hello, World!"
print(a.replace("H", "J"))

#split 
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#print format strign 
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#format multiple lines
quantity = 3
itemno = 567
price = 49.95
print(f"i want (quantity)")
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#also give the order 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#escape charther
txt = "We are the so-called \"Vikings\" from the north."

#start with c
msg.startwith("c")

#end with c
msg.endwith("c")

#also for word

#only charather alpha
msg.isalpha() 

#only numbers
msg.isdecimal()

#or number or letters
msg.isalnum()

#find if there is a space 
msg.isspace()

#split()
msg= "132343-345435435-4-5435435"
series_num=msg.split("-")

#join() from list to string
hw = ["1","2","3"]
string = ",".join(hw)