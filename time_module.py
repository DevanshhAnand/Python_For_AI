# strategy to find how much time does a program -> run it 1500 times and take out the average of the 1500 times 
import time

inital=time.time()
k=0
while(k<45):
    print("I'm a billionaire")
    time.sleep(1)
    k+=1
whileran=time.time()-inital
print("While loop ran in",whileran,"seconds")

inital2=time.time()
for i in range(45):
    print("I'm a billionaire")
forran=time.time()-inital2
print("For loop ran in ",forran,"seconds")

if(whileran>forran):
    print("While is faster")
elif(whileran<forran):
    print("For is faster")
else:
    print("Both take same time")
 
# Sleep function will sleep the processor for some time you have given
# LOCAL TIME
localtime=time.asctime(time.localtime(time.time()))
print(localtime)



