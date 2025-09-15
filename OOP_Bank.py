class BankApp:
    def __init__(self,acn,name,balance):
        self.acn=acn
        self.name=name
        self.balance=balance
    def deposit(self,amount):
       if amount>0 and amount<100000:
           self.balance+=amount
           print("Amount deposited successfully")
       else:
              print("Invalid amount")
              
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance or invalid amount")  
    def display_info(self):
        print("Account number:{}".format(self.acn))
        print("Account holder name:{}".format(self.name))
        print("Balance:{}".format(self.balance))

b1=BankApp(2020122004,"RAM",5000)
while True:
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        amount=int(input("Enter amount to deposit:"))
        b1.deposit(amount)    
    elif choice==2:
        amount=int(input("Enter amount to withdraw:"))
        b1.withdraw(amount)
    elif choice==3:
        b1.display_info()       
    elif choice==4:
        print("Thank you for using the bank app")
        break   
    else:
        print("Invalid choice")                    