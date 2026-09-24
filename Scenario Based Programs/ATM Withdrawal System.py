"""ATM Withdrawal System
The following program allows a user to withdraw money until they choose to exit.
Initial amount in 10,000. The program does the following:
    Display a menu: Withdraw, Check Balance, Exit.
    If the user selects Withdraw, ask for an amount.
    Check whether the amount is positive and whether sufficient balance is available.
    Update the balance after a successful withdrawal.
    Continue showing the menu until the user selects Exit"""

balance = 10000.00
choice = 0
while choice != 3:
    print("MENU\n1. Withdraw Money\n2. Check Balance\n3. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        amt = float(input("Enter amount to be with drawn: "))
        if amt < 0:
            print("Negative Amount!! Try again")
        elif amt > balance:
            print("Amount is greater than Initial Amount. Try again")
        else:
            print("Withdrawn Successfully")
            balance -= amt

    elif choice == 2:
        print(f"Balance: {balance}")

    elif choice == 3:
        print("Thank you for using our ATM.\nWe hope to see you again")

    else:
        print("Invalid input. Try again")
    print()
