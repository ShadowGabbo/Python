class Student:
    #crate a var for all the istances
    hour = 36
    total_student = 0

    def __init__(self,name,surname,course):
        self.name = name
        self.surname = surname
        self.course = course
        Student.total_student+=1
    
    def personal_scheldue(self):
        return f"Personal info:\nName:{self.name}\nSurname:{self.surname}\nCourse:{self.course}\nHours per week:{self.hour}\n"#access to the var of class
        #or
        #self.hour 
    


stundent_one = Student("Py","Mike","Programming")
stundent_two = Student("Marta","Stannis","Science")



stundent_one.hour+=4 

print(stundent_one.personal_scheldue())
print(stundent_two.personal_scheldue())
print("Total students: ",Student.total_student)