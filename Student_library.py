class Library:
    def __init__(self, listOfBooks):
        self.books= listOfBooks
        
    def displayAvailableBooks(self):
        print("Books Present in this library are:")
        for book in self.books:
            print("\t ->"+book)
            
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been Issued{bookName}.Please Keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False
        
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks For Returning this book! Hope You Enjoyed reading it.Have a great day Ahead!")
            
class Student:
    def requestBook(self):
        self.book= input("Enter the name of the Book you want to Borrow: ")
        return self.book
    def returnBook(self):
        self.book= input("Enter the name of the Book you want to Return: ")
        return self.book
    

if __name__=="__main__":
    centralLibrary = Library(["Algorithms","Django", "Clrs","Python notes"])
    student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        WelcomeMSG ='''====WELCOME TO CENTRAL LIBRARY====
        PLEASE CHOOSE AN OPTION:
        1. LIST ALL THE BOOKS
        2. REQUEST A BOOK
        3. ADD/RETURN A BOOK
        4. EXIT THE LIBRARY
        '''
        print(WelcomeMSG)
        a=int (input("Enter a choice:  "))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks For Choosing Central library.Have a great day ahead!4")
            exit()
        else:
            print("Invalid Choice!")
        