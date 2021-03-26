There are four collection data types in the Python programming language:
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered and changeable. No duplicate members.

#LIST

#This is a comment
names = ["Harry", "Hermione", "Ron"]
print(names)

#add an element
names.append("Draco")
print(names)

#remove an element 
names.remove("key")
print(names)

#sort
names.sort()
print(names)

#reverse
names.sort(reverse=True)

#index
names.index(key)

#list allow duplicate values 

#list length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#list are objects

#list constructor 
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#access item
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#negative item
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#slicing staff that i already know

#check if item exist
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#change iteam in lists
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#insert an element in a list 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
thislist[2]= "watermelon"
print(thislist)

#extend a list from an existing one
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#for range in a list
for primo in primi:
    print(primo)

#also
lista_numerica = list(range(99,300))

#list in list
multiple = [1,23,[1,2,3]]
print(multiple[2][2])