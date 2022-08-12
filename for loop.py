# list1 = [["harry",2],["harry",2],["harry",2],["harry",2]]

# length=len(list1)
# for item in list1:
#     print(item,end=",")
#     if item=="\0":
#         print('devansh')
#
# n = int(input())
# n1 = 0
# while n1 != n:
#     print(n1+1, end="")
#     n1 += 1
# xyz=0
# for xyz,lollypop in list1:
#     print(xyz,"eats",lollypop)
# quiz: make a list that contains randomize number,string but print only those elements which are greater than 6
listq=["devabnahjughu",6,465,345663,7897,3.22,1]
for i in listq:
    if str(i).isnumeric() and i>=6:
        print(i)
