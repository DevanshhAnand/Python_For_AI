def searchname():
    # name=input("Enter your name to find whether it is present inside our list or not: ")
    import time
    f= open("names.txt")
    x=f.read()
    y=input("Enter ur name: ")
    if y in x:
        print('found')
    else:
        print('not fouund')

searchname()


# coroutine
def searcher():
    print("Reading the File wait for a while")
    f= open("names.txt")
    x=f.read()
    print("File Readed !!")
    
    while(True):
        text = (yield)
        if text in x:
            print("Your Name is Found in the File.")
        else:
            print("Your Name is not Found in the File.")

name = input("Enter the Name you want to Search - ")
search = searcher()
print("Search Started")
next(search)
search.send(name)