# Operator overloading is used to over load the built in fuction like add,sub..etc... for objects
# because object are not allowed to perform operation on operators

from msilib.schema import Class


class A:
    no_of_leaves=7

    def __init__(self,leaves):
        self.no_of_leaves=leaves
    
    def __add__(self,other):
        return self.no_of_leaves + other.no_of_leaves
class B:
    no_of_leaves=7
    def __init__(self,leaves):
        self.no_of_leaves=leaves
a= A(45) 
b = B(45) 
print(a+b)      

