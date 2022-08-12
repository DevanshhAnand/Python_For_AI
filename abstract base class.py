from abc import ABCMeta,abstractmethod

# This is known as abstract class which used like a which is the leader and have some set of rules which have to there in inherited class
# for example this class shape is the leader of all the shape that exist in real world and have rule that every which will inehrit it have to contain the printarea function else it will throw errors

#you can't make objects of abstract class or the leader class as per example

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):  
    type="Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7
    
    def printarea(self):
        return self.length*self.breadth

rectangle = Rectangle()
print(rectangle.printarea())
