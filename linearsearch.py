def linearsearch(a,x,i=0):
    if i==len(a):
        return -1
    if a[i]==x:
        return i
    return linearsearch(a,x,i+1)

a=list(map(int,input().split()))
x=int(input())
index=linearsearch(a,x)
if index==-1:
    print("Element not found")
else:
    print("Element found at index",index)
