from statistics import harmonic_mean
from unicodedata import name


class Employee:
    no_of_leaves=5
    
    def printdetails(self):
        print(self.name)
        print(self.std)
    
    def __init__(self,name,std):#constructor
        self.name=name
        self.std=std
        
    @classmethod
    def from_str(cls,string):#alternative constructor
        # params=string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
    
    @classmethod#This is class mehtod to change attribute of the class
    def change_leaves(cls, newleaves):
        cls.no_of_leaves=newleaves

harry=Employee("Devansh",1000000 )
rohan=Employee.from_str("Rohan-1000")
harry.printdetails()
rohan.printdetails()
harry.change_leaves(556545)
print(Employee.no_of_leaves)