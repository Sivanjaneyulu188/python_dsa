
bill=0
choice = input("Do you want to order: Y/N ")
while choice=='Y' or choice=='y':
    print("Menu: ")
    print("1. WATERBOTTLE")
    print("2. FRIDERICE")  
    print("3. NOODLES")
    print("4. Exit")
    n=int(input("Enter your choice: "))
    if n==1:
        q=int(input("Enter quantity: "))
        bill+=q*20
    elif n==2:
        q=int(input("Enter quantity: "))
        bill+=q*80
    elif n==3:
        q=int(input("Enter quantity: "))
        bill+=q*90
    elif n==4:
        break
print("Total bill is: ",bill)