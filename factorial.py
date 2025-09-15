def get_fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*get_fact(n-1)

n=int(input("Enter a number: "))
print(get_fact(n))