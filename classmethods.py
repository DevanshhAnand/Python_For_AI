class Students:
    no_of_leaves=6

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves=new_leaves

rohan=Students()
rohan.change_leaves(45)#this will the change the value of orignal variable present in class
print(rohan.no_of_leaves)
print(Students.no_of_leaves)
