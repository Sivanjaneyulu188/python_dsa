def reverseofnum(n,rev):
    if n==0:
        return rev
    else:
        rev=rev*10+(n%10)
        return reverseofnum(n//10,rev)    
n=int(input("Enter a number: "))
print(reverseofnum(n))