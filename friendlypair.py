num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
divisorsofnum1=0
divisorsofnum2=0
if num1!=0:
    for i in range(1,num1+1):
        if num1%i==0:
            divisorsofnum1+=i
if num2!=0:
    for i in range(1,num2+1):
        if num2%i==0:
            divisorsofnum2+=i
        
if (divisorsofnum1)/num1 == (divisorsofnum2)/num2:
    print("Friendliy Pair")
else:
    print("Not a Friendly Pair")