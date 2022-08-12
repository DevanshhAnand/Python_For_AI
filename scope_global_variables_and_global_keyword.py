l = 10 #global variable

def func1(n):
    # l=5#local variable
    # m=8#lcoal variable
    # as if you know you cant chagne global variable as like local variable you need special permission for that so this:
    global l#by doing this now you can change the global but it should not be done frequently because changing global variable is not a good practice
    l=l+20
    print("after giving special permission (this is global variable): ",l)
    # print("local variable ",l)

print("global variable ",l)