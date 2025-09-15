n=int(input("Enter a number: "))
even_sum=0
even_place=1
while n>0:
    digit=n%10
    if digit%2==0:
        even_sum+=digit*even_place
        even_place*=10
    n=n//10
print("Difference between even and odd place values is:",even_sum)