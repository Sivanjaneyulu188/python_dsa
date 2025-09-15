n=int(input("Enter n value: "))
temp=n
sum=0
power=1
while n>0:
    digit=n%10
    sum+=digit**power
    n=n//10
    power+=1
if sum==temp:
    print("It is an correct number")
else:
    print("It is not correct number")
    