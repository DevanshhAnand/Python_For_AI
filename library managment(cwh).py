# make a library management system with 4 functiuons 1.display book 2.lend book 3.add book 4.return book

from asyncio.windows_events import NULL
from dis import dis
from selectors import SelectorKey

listofbooks=["bhagwat geeta","million stars","rich dad poor dad","calculus"]
bookname = NULL
addbookname = NULL
username = NULL
returnbookname = NULL
dictionary = {}
class Library:
    
    lobs = ["xyz"]
    libname='OWN'
    def __init__(self,lob,libraryname):
        self.lobs=lob
        self.libname=libraryname
        while(True):
            username=input("Enter your name: ")
            userinput=input("Enter the operation you want to perform: ")
            if userinput == 'display':
                self.display()
            elif userinput=='lend books':
                self.lendbooks()
            elif userinput == 'add book':
                self.addbook()
            elif userinput=='return book':
                self.returnbook()
            else:
                print('Try Performing existing operation')

    def display(self):
        print("List of books\n")
        for i in self.lobs:
            print(i)


    def lendbooks(self):
        self.display()
        username = input("Enter your name: ")
        bookname = input("Enter the name of book you want: ")
        booknamelow = bookname.lower()
        if booknamelow in listofbooks:
            print('found')
            dictionary[username] = booknamelow
            self.lobs.remove(booknamelow)
        else:
            print('not found')

        print("Thanks Visit Again!")
        self.display()


    def addbook(self):
        addbookname = input("Enter the name of the book which you want to add: ")
        addbooknamelow = addbookname.lower()
        print(self.lobs)
        self.lobs.append(addbooknamelow)
        print("Thank you for donating books")


    def returnbook(self):
        returnbookname = input("Enter the name of the book you want to return: ")
        returnbooknamelow = returnbookname.lower()
        self.lobs.append(returnbooknamelow)
        print("Thanks for returning")
    

harrylibrary=Library(['bhagwat geeta','million stars'],"LibraryX")           










# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input


# class Library:
#     def __init__(self, list, name):
#         self.booksList = list
#         self.name = name
#         self.lendDict = {}

#     def displayBooks(self):
#         print(f"We have following books in our library: {self.name}")
#         for book in self.booksList:
#             print(book)

#     def lendBook(self, user, book):
#         if book not in self.lendDict.keys():
#             self.lendDict.update({book:user})
#             print("Lender-Book database has been updated. You can take the book now")
#         else:
#             print(f"Book is already being used by {self.lendDict[book]}")

#     def addBook(self, book):
#         self.booksList.append(book)
#         print("Book has been added to the book list")

#     def returnBook(self, book):
#         self.lendDict.pop(book)

# if __name__ == '__main__':
#     harry = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "CodeWithHarry")

#     while(True):
#         print(f"Welcome to the {harry.name} library. Enter your choice to continue")
#         print("1. Display Books")
#         print("2. Lend a Book")
#         print("3. Add a Book")
#         print("4. Return a Book")
#         user_choice = input()
#         if user_choice not in ['1','2','3','4']:
#             print("Please enter a valid option")
#             continue

#         else:
#             user_choice = int(user_choice)


#         if user_choice == 1:
#             harry.displayBooks()

#         elif user_choice == 2:
#             book = input("Enter the name of the book you want to lend:")
#             user = input("Enter your name")
#             harry.lendBook(user, book)

#         elif user_choice == 3:
#             book = input("Enter the name of the book you want to add:")
#             harry.addBook(book)

#         elif user_choice == 4:
#             book = input("Enter the name of the book you want to return:")
#             harry.returnBook(book)

#         else:
#             print("Not a valid option")


#         print("Press q to quit and c to continue")
#         user_choice2 = ""
#         while(user_choice2!="c" and user_choice2!="q"):
#             user_choice2 = input()
#             if user_choice2 == "q":
#                 exit()

#             elif user_choice2 == "c":
#                 continue

