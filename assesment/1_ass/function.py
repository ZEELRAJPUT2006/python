bookdata = {}  

def book_rental_details():
    """ ******** customer details ***** """
    Customer_name = input("Enter your name: ")
    Book_title = input("Enter the book title: ")
    Rental_date = input("Enter the date: ")
    Expected_return_date = input("Enter the return date: ")

    bookdata.update({
        Customer_name: {
            "Book_title": Book_title,
            "Rental_date": Rental_date,
            "Expected_return_date": Expected_return_date
        }
    })


def view():
    # print(""" ****** view details ****** """)
    if not bookdata:
        print("No records found.")
    else:
        for i, j in bookdata.items():
            print(f"\nCustomer name: {i}")
            for x, y in j.items():
                print(f"{x} : {y}")

def bookreturn():
    print("******************* Book Return Details ************************************")
    Cname = input("Enter your name: ")

    if Cname in bookdata:
        book = bookdata[Cname]

        print("\n ======== Book Return ========= ")
        print(f"Cname : {Cname}")
        print(f"Book_tile : {book['Book_title']}")
        print(f"Rental date : {book['Rental_date']}")
        print(f"Expected_return_date : {book['Expected_return_date']}")

        current_date = input("enter the current date : ")

    e_year, e_month, e_day = map(int, book['Expected_return_date'].split('-'))
    c_year, c_month, c_day = map(int, current_date.split('-'))

    delay = (c_year - e_year) * 365 + (c_month - e_month) * 30 + (c_day - e_day)

    fine_per_day = 10
    fine = 0
    if delay > 0:
            fine = delay * fine_per_day

            print("\n ============ Summary Receipt ============ ")
            print(f"Customer name : {Cname}")
            print(f"Book title    : {book['Book_title']}")
            print(f"Rental_date   : {book['Rental_date']}")
            print(f"Return_date   : {current_date}")
            print(f"Delay (days)  : {delay if delay > 0 else 0}")
            print(f"Late fee      : Rs.{fine}")
            print("==========================================")
            print("\n  Thank you for visiting ReadEase Library")

            del bookdata[Cname]
    else:
        print("No record found")



       