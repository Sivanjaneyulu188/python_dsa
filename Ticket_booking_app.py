def superLuxury():
    tickets=int(input("Enter the number of tickets: "))
    if tickets<=6 and tickets>0:
        bill=tickets*550
    else:
        print("Cannot book more than 6 tickets")
    return bill
def indra():
    tickets=int(input("Enter the number of tickets: "))
    if tickets<=6 and tickets>0:
        bill=tickets*680
    else:
        print("Cannot book more than 6 tickets")
    return bill
def sleeper():
    tickets=int(input("Enter the number of tickets: "))
    if tickets<=6 and tickets>0:
        bill=tickets*400
    else:
        print("Cannot book more than 6 tickets")
    return bill
tc=0
while True:
    print("1. Super Luxury")
    print("2. Indra")
    print("3. Sleeper")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        tc=superLuxury()
    elif choice == 2:
        tc=indra()
    elif choice == 3:
        tc=sleeper()
    elif choice == 4:
        print("Thank you")
        break
    else:
        print("Invalid choice")
if tc>1000:
    tc=tc-(tc*0.1)
gst=tc*0.05
tolltax=tc*0.02
total=tc+gst+tolltax
print("GST:",gst)
print("Toll tax:",tolltax)  
print("Total bill:",total)  