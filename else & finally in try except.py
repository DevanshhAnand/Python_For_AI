f1 = open("mylogs.txt")

try:
    print("hello")
    # f=open("does.txt")
except Exception as e:
    print(e)
except EOFError as e:
    print("EOFerror aa gya hai bhai")
except IOError as e:
    print("IOEerror agya hai bhai")
else:
    print("This will run only if except is not running and vice versa")
finally:
    print("Run this anyway...")
    f1.close()

print("At the end")