"""Movie Ticket Booking System
This program asks the user for name and age continuously and displays
the price for the person based on his/her age
    Below 5 years: Free
    5-17 years: ₹100
    18-59 years: ₹200
    60 years and above: ₹120"""

entry = True
while entry:
    error = False
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    print(f"Hello {name}!")

    # Checking for price based on age
    if 0 <= age < 5:
        print("Ticket Price: Free")

    elif 5 <= age <= 17:
        print("Ticket Price: Rs. 100")

    elif 18 <= age <= 59:
        print("Ticket Price: Rs. 200")

    elif age >= 60:
        print("Ticket Price: Rs. 120")

    else:
        print("Invalid Age!! Try Again...")
        error = True

    # Does the user want to continue
    if not error:
        print("Payment done!")
        cont = input("Do you want to continue(yes/no): ")
        if cont == "yes":
            entry = True
        else:
            entry = False
            print("Thank you. Bye")
