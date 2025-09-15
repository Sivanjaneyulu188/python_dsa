n=int(input("Enter n value: "))
temp=n
sum=0
c_of_digits=len(str(n))
power=c_of_digits
while n>0:
    digit=n%10
    sum+=digit**power
    n=n//10
    power-=1
if sum==temp:
    print("It is a Disarium number")
else:
    print("It is not a Disarium number")
    