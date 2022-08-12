# def funargs(food):
#     for items in food:
#         print(items)

# fruits = ["apple", "banana", "cherry","aijgia"]
# funargs(fruits)



#-> RULE FOR GIVING ARGUMENT IN NORMAL,ARGS,KWARGS



def funargs(normal,*args,**kwargs):
    print(normal)
    for items in args:
        print(items)
    print("\nUsecase of the fruits: ")
    for keys,value in kwargs.items():
        print(f"{keys} -> {value}" )

normal="This is a normal string"
fruits = ["apple", "banana", "cherry","aijgia"]
dictionary={"Apple":"Good for lungs",
            "banana":"Good for stamina"}
funargs(normal,*fruits,**dictionary)