# classes- Template
# object - instance of the class

# DRY - Do not repeat yourself

class Student:#always write class name with capital letter
    # name=input("Enter Your Name: ")
    # std=int(input("Enter Your Class: "))
    # Section=input("Enter your class Section: ") 
    def printdetails(self):#functions created in class are known as methods
        print(self.name)
        print(self.std)
        print(self.Section)
    def __init__(self, name,std,section):#CONSTRUCTOR
        self.name=name
        self.std=std
        self.Section=section
harry=Student("devansh",4,"L")
harry.subjects=["Maths","Hindi","Machine Learning"]
# print(harry.subjects)

# class variable - property which are of class for example name,std,section are the property of class and they cannot be changed through object it can be only changed by classes objects can only read them 
# harry.name="bhauu"#this is instance variable with same name as class variable "name"
# print(harry.__dict__)#this will give all the variable of the objects and its values
# print(Student.name)

print(harry.printdetails())