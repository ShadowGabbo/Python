people = [
    {"hey":"ciao", "hey":"fra"},
    {"hey":"noo", "hey":"hey"}
]

def f(person):
    return person["name"]

people.sort(key= lambda person: person["hey"])

print(people)