def deposit(balance):
    amount = int(input("Enter the amount to deposit: "))
    print("Avilable balance:", balance + amount)
    balance= balance + amount
    return balance

    
def withdraw(balance):
    amount = int(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds")
    else:
        balance = balance - amount
        print("Available balance:", balance)
    return balance
    
def check_balance(balance):
    print("Available balance:", balance)
    return balance  
balance=int(input("Enter the initial balance: "))
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        balance = deposit(balance)
    elif choice == 2:
        balance=withdraw(balance)
    elif choice == 3:
        check_balance(balance)
    elif choice == 4:
        print("Thank you")
        break
    else:
        print("Invalid choice")
