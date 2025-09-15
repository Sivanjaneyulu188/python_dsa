n=int(input("Enter a number: "))
even_sum=0
odd_sum=0
even_place=1
odd_place=1
while n>0:
    digit=n%10
    if digit%2==0:
        even_sum+=digit*even_place
        even_place*=10
    else:
        odd_sum+=digit*odd_place
        odd_place*=10
    n=n//10

total_diffrence=even_sum-odd_sum
print("Difference between even and odd place values is:",total_diffrence)