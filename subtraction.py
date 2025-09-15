def sub(a,b):
    if b==0:
        return a
    else:
        return sub(a-1,b-1)


a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(sub(a,b))








