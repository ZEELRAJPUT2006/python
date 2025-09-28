from function import book_rental_details, view, bookreturn

print(" ============================= WELCOM TO READEASE LIBRARY =============================")
ans = 'y'

while ans != 'n':  
    print("""
            
            1. Book Rental Booking
            2. Book Return and Late Fees Calculation
    """)
    choice = int(input("Enter your choice: "))  

    if choice == 1:
        ans1 = 'y'
        while ans1 != 'n': 
            print("""
                    1. Book rental details
                    2. View
            """)
            b_choice = int(input("Enter your choice: "))

            if b_choice == 1:
                book_rental_details()
            elif b_choice == 2:
                print(" ***************** Book details *************************")
                view()
            else:
                print("Invalid choice")

            ans1 = input("Do you want to continue menu? (y/n): ")

    elif choice == 2:
            bookreturn()


    ans = input("Do you want to continue main menu? (y/n): ")
