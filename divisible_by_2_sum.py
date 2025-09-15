n=int(input("Enter a number: "))
sum=0
while n>0:
    digit=n%10
    if digit%2==0:
        sum+=digit
    n=n//10
print("Sum of even digits is:",sum)