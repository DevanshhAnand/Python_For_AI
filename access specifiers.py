class access_specifiers:
    public=1
    _protected=2
    __private=3
    def printprivatevar(self):
        print(self.__private)

harry = access_specifiers()
print(harry.public)
print(harry._protected)
# print(harry.__private)#This cannot be accessed as it is private variable of class. It can be only accessed by the class methods or say class function
harry.printprivatevar()
print(harry._access_specifiers__private)#This is second method for accessing private variables 
# This method is known as name mangling 

 