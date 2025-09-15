def sumofdigits(n,s=0):
    if n==0:
        return s
    else:
        digit=n%10
        s=s+digit
        return sumofdigits(n//10,s)

n=int(input("Enter a number: "))
print(sumofdigits(n))