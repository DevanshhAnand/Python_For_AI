# recursive terminology:
# n! = n-1 * n-2 *n-3....1  iterative method
# n! = (n-1)! recursive method
    # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120

def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)

def factorial_iterative(n):
    fac=1
    for i in range(1,n+1):
        fac *= i
    return fac
def fibonnaci_iterative(n):
    prev=0
    current=1
    print(prev,current,end=" ")
    for i in range(2,n):
        prevprev=prev
        prev = current
        current=prev+prevprev
        print(current,end=" ")
    return current
def fibonnaci_recursive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonnaci_recursive(n-1)+fibonnaci_recursive(n-2)
number = int(input("Enter the number: "))
# print("Using iterative method",factorial_iterative(number))
# print("using recursive method",factorial_recursive(number))
print("Fibonnaci using iterative: ",fibonnaci_iterative(number))
# print("Fibonnaci using recursive: ",fibonnaci_recursive(number))