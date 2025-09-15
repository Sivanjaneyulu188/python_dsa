# n=12345
# first=n%10
# last=n//10000
# print(first+last)
import math
n=int(input("Enter n value: "))
last=n%10 
first=n//(10**(int(math.log10(n))))
print("Sum is",first+last)