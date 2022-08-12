from ast import Num


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

class Students:
    num=78
class programmer(Employee,Students):#multiple inheritance
    def programmersal(self):
        print(self.no_of_leaves)
        print(self.num)

harry=programmer("harry",3454)
harry.programmersal()