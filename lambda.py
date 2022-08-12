# lambda functions are also known as anoynomus function
# def minus(a , b):
#     return a+b
# minus = lambda a,b:a-b #lambda functiions are used for making short hand functions
# a=8
# b=9
# print(minus(a,b))
sorti=lambda list1:list1[1]
list1=[[23,53],[4,3],[354,1]]
# list1.sort(key=lambda list1:list1[1])
# OR
list1.sort(key=sorti)
print(list1)