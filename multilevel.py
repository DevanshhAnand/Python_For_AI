from cgi import print_arguments


class Father:
    Basketball = 1
    def __init__(self, skills):
        self.Basketball=skills
        print(self.Basketball)  

class Son(Father):
    Cricket=1
    def printskills(self):
        print("Basketball: ",self.Basketball)
        print("Cricket: ",self.Cricket)
class Grandson(Son):
    Volleyball=1
    def printskills(self):
        print("Volleyball: ",self.Volleyball)
        return super().printskills()

Larry = Father()
# Garry = Son(2)
# Harry = Grandson()

# Harry.printskills()
