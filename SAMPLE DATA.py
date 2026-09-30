### SAMPLE DATA
books = ["ATOMIC HABITS","1984","THE GREAT GATSBY","IKIGAI","THE ALCHEMIST","THE PSYCHOLOGY OF MONEY"] # available books
taken = []          # borrowed books


def addBook():
    name = input("Enter the name of the book to add: ")
    a = name.upper()
    books.append(a)
    print(a, "has been added.\n")


def showBook():
    if len(books) == 0:
        print("Library is empty right now.\n")
    else:
        print("\nBooks present in library:")
        for idx, b in enumerate(books):
            print(idx + 1, "-", b)
        print()


def borrowBook():
    name = input("Which book do you want to borrow?(Name) ")
    a = name.upper()

    if a in books:
        books.remove(a)
        taken.append(a)
        print("You borrowed:", a, "\n")
    else:
        print("Sorry, this book is unavailable. It will be available soon.\n")
def returnBook():
    name = input("Enter the book you want to return: ")
    a=name.upper()
    

    if a in taken:
        taken.remove(a)
        books.append(a)
        print("Returned:", a, "\n")
    else:
        print("You didn't borrow this book.\n")


# menu
while True:
    print("LIBRARY MANAGEMENT SYSTEM")
    print(" Library's menu ")
    print("1. Add A Book")
    print("2. Show Available Books")
    print("3. Borrow A Book")
    print("4. Return A Book")
    print("5. Quit")

    choice = input("Choose any option number(1-5):")
    if choice == "1":
        addBook()
    elif choice == "2":
        showBook()
    elif choice == "3":
        borrowBook()
    elif choice == "4":
        returnBook()
    elif choice == "5":
        print("Thank you for using my library.")
        break
    else:
        print("Invalid option. Try again.\n")