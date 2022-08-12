# f = open("trial.txt","w")#this will overwrite the existing file past writeen will be deleted
# # f = open("trial.txt","a")#this will add the content
# a=f.write("harry bhai is the best")
# print(a)#this will give the no. of characters you have written in a file
# f.close()

#handle read and write both
from tkinter import Y


f= open("trial.txt","r+")
x=f.read()
y='harry'
if y in x:
    print('found')
f.write("Thank you")