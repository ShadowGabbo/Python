houses = {"Harry": "Gryffindor", "Draco":"Slytherin"}

print(houses["Harry"])

#add elements
houses["hermione"]="Gryffindor"

print(houses)

#check if an element is in the dic
"key" in dict 

#delete element
del dict[key]

#metodo keys()
#obtain a list of all the keys
dict_name.keys()

#metodo values()
#obtain a list of all the values
dict_name.values()

#metodo items()
#obtain a list of all the items , key values
dict_name.keys()

#loop in keys
for keys in dict_name:
    print(chiave)

if "key" in dict_name:
    print(dict_name[key])
else:
    print("key not find")

#get method
#more cool doing
dict_name.get("key",msg)#give the value if exist or the msg after

#set defualt 
#if doesnt exist create the couple key/value
dict_name.setdefault(key,value)


