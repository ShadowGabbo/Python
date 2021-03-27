class Person:
    #crate a var for all the istances
    hour = 36
    total_student = 0

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    def personal_scheldue(self):
        return f"Personal info:\nName:{self.name}\nSurname:{self.surname}\n"

#heredity from Person
class Student(Person):
    profile = "Student"

    def __init__(self,name,surname,course):
        super().__init__(name,surname)#link to the attributes of the superclass Person
        self.course = course 

    def personal_scheldue(self):
        scheldue = f"Profile:{Student.profile}\nCourse:{self.course}\n"
        return super().personal_scheldue() + scheldue

    def change_course(self,course):
        self.course = course
        print("-Course Updated-\n")

    pass #can access to methods and attributes of Person

class Teacher(Person):
    profile = "Teacher"

    def __init__(self,name,surname,classes):
        super().__init__(name,surname)#link to the attributes of the superclass Person
        if classes is None:
            self.classes = []
        else:
            self.classes = classes

    def personal_scheldue(self):
        scheldue = f"Profile:{Teacher.profile}\nClasses:{self.classes}"
        return super().personal_scheldue() + scheldue
    
    def add_class(self,new):
        if new not in self.classes:
            self.classes.append(new)
            print("\n-Added a class-")

    pass #can access to methods and attributes of Person

student_one = Student("Gabriele","Sarti","Programming")
teacher_one = Teacher("Mattia","Oldani",["Python","C++"])
print(student_one.personal_scheldue())
print(teacher_one.personal_scheldue())

teacher_one.add_class("C")
student_one.change_course("Philosophy")
print(student_one.personal_scheldue())
print(teacher_one.personal_scheldue())
#print(help(Student))