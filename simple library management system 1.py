class library:
    def __init__(self, books):
        self.books = books

    def list_books(self):
        print("Available books")
        for book in self.books:
            print(book)

    def borrow_book(self, borrow_book):
        if borrow_book in self.books:
            print("Get your Books now")
            self.books.remove(borrow_book)
        else:
            print("Book not Available")

    def receive_book(self, receive_book):
        print("You have returned the book")
        print("important newsplease enter the number of the days to retun:")
        days = int(input("Enter the number of the days:"))
        if days <= 0 and days >= 5:
            fine = days * 1
            print("Fine:", fine)
        elif days >= 6 and days <= 10:
            fine = days * 10
            print("Fine", fine)
        print("You have returned the books")
        self.books.append(receive_book)


books = ["c", "c++", "Java"]
o = library(books)
msg = """
    1.display books
    2.borrow books
    3.retuen books
"""
while True:
    print(msg)
    ch = int(input("Enter the choice:"))
    if ch == 1:
        o.list_books()

    elif ch == 2:
        book = input("Enter book name to borrow:")
        o.borrow_book(book)

    elif ch == 3:
        book = input("Enter book name to return:")
        o.receive_book(book)

    else:
        print("Thank you come again")
        quit()
