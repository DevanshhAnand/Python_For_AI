from cProfile import run
import random
from secrets import choice

list1=["s","p","sc"]


userwin=0
computerwin=0
run_time=1
while(run_time<=10):

    usermove= input("Enter your move: ")
    usermove.lower()

    choice = random.choice(list1)

    print("Computer's Move: ",choice)
    print("User's Move: ",usermove)

    if usermove==choice:
        print("Tie")
    elif usermove==list1[0] and choice==list1[1]:
        print("Computer wins")
        computerwin+=1
    elif usermove==list1[0] and choice==list1[2]:
        print("you win")
        userwin+=1
    elif usermove==list1[1] and choice==list1[0]:
        print("you win")
        userwin+=1
    elif usermove==list1[1] and choice==list1[2]:
        print("computer win")
        computerwin+=1
    elif usermove==list1[2] and choice==list1[0]:
        print("computer win")
        computerwin+=1
    elif usermove==list1[2] and choice==list1[1]:
        print("you win")
        userwin+=1
    else:
        print("Something Went Wrong")
    
    run_time+=1

if (userwin>computerwin):
    print("User wins by ",userwin," times")
    print("Computer losses by ",computerwin," times")

elif(userwin<computerwin):
    print("Computer wins by ",computerwin," times")
    print("User losses by ",userwin," times")

elif(userwin==computerwin):
    print("Tie")