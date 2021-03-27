#class
class Student:
    #create a costructor, inizialize self 
    def __init__(self,name,surname,course):#var of instance
        #attributes
        self.name = name
        self.surname = surname
        self.course = course
    
    def personal_scheldue(self):
        return f"Personal info: \nName:{self.name}\nSurname:{self.surname}\nCourse:{self.course}"
    #2 methods

#crate a instance
stundent_one = Student("Py","Mike","Programming")
stundent_two = Student("Marta","Stannis","Science")

print(stundent_one.personal_scheldue())
print(stundent_two.personal_scheldue())

#or
print(Student.personal_scheldue(stundent_one))