class library:
    def __init__(self, bookList):
        self.books = bookList

    def displayAvailableBooks(self):
        print("Books present in this library are : ")
        for book in self.books:
            print("=>\t"+book)

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(f"You have been issued the book {bookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print(f"Sorry! either the book {bookName} not present in library or the book has already been issued by someone esle.")
            return False

    def returnBooks(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book. Hope you enjoyed reading it.")


class student:
    def requestBooks(self):
        self.book = input("Enter the name of book you want to Borrow.\n")
        return self.book

    def returnBooks(self):
        self.book = input("Enter the name of book you want to Add/Return.\n")
        return self.book


if __name__ == "__main__":
    mainLibrary = library(["Algorithms", "Python", "Java", "Let us C"])
    Student = student()

    while True:
        welcomeMSG = '''\n################## Welcome To Central Library ##################
        Please choose an option by pressing key:
        1 for Display all books of library
        2 for Request book
        3 for Add/Return book
        4 for Exit form library
        '''
        print(welcomeMSG)
        a = int(input("Enter a choice :"))
        if a == 1:
            mainLibrary.displayAvailableBooks()
        elif a == 2:
            mainLibrary.borrowBooks(Student.requestBooks())
        elif a == 3:
            mainLibrary.returnBooks(Student.returnBooks())
        elif a == 4:
            print("Thanks for using this library")
            exit()
        else:
            print("Invalid Choice")
