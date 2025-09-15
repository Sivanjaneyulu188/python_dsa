def add(a,b):
    if b==0:
        return a
    else:
        return add(a+1,b-1)


a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(add(a,b))