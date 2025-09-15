amount=int(input("Enter amount: "))
if amount%100!=0:
    print("Invalid amount")
else:
    if amount>=500:
        fivehundred=amount//500
        amount=amount%500
        print("500=",fivehundred)
    if amount>=200:
        twohundred=amount//200
        amount=amount%200
        print("200=",twohundred)            
    if amount>=100:
        onehundred=amount//100
        amount=amount%100
        print("100=",onehundred)