def opposite (a,b):
    if (a<0 and b>0):
        return True
    elif (a>0 and b<0):
        return True
    else:
        return False


num1=int(input("num1"))
num2=int(input("num2"))

print(opposite(num1 , num2))
