class Person:
    hour = 36
    total_student = 0

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    #a method of the class not linked to the attributes 
    @classmethod #decorator create a method of the class that pass a class and not a instances
    def fromStringng(cls,string_person,*args):#op skill
        name,surname = string_person.split("-")
        return cls(name,surname,*args)

    @classmethod
    def occupy(cls):
        if cls.__name__=="Student":
            return "Student"
        else:
            return "Teacher"
    
    pass

    def personal_scheldue(self):
        return f"Personal info:\nName:{self.name}\nSurname:{self.surname}\n"

class Student(Person):
    profile = "Student"

    def __init__(self,name,surname,course):
        super().__init__(name,surname)
        self.course = course 

    def personal_scheldue(self):
        scheldue = f"Profile:{Student.profile}\nCourse:{self.course}\n"
        return super().personal_scheldue() + scheldue

    def change_course(self,course):
        self.course = course
        print("-Course Updated-\n")

    pass 

class Teacher(Person):
    profile = "Teacher"

    def __init__(self,name,surname,classes):
        super().__init__(name,surname)
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
    pass 

student_one = Student("Gabriele","Sarti","Programming")
teacher_one = Teacher("Mattia","Oldani",["Python","C++"])
print(student_one.personal_scheldue())
print(teacher_one.personal_scheldue())

teacher_one.add_class("C")
student_one.change_course("Philosophy")
print(student_one.personal_scheldue())
print(teacher_one.personal_scheldue())

print("\nPART TWO\n")
iroman = "TONY-STARK"
person1 = Student.fromStringng(iroman,"Se0")
print(person1.personal_scheldue())

person2 = Teacher.fromStringng(iroman,"Bio")
print(person2.personal_scheldue())


print("\nOccupy person1: "+person1.occupy())
print("Occupy person2: "+person2.occupy())