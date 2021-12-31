class Library:
    def __init__(self, list_of_books, Name_of_Library):
        self.BookList = list_of_books
        self.Name_of_Library = Name_of_Library
        print(f"\n\t\t\t\t\t\t\t\t\t Welcome to the {self.Name_of_Library} \n There are various Provided by us")

    def DisplayBooks(self):
        print("\t\t\t\t\t\t\t\t***************Books are Available at Here!!***************\n")
        for i in self.BookList:
            print(f" {i}")
            print("-------------")

    def AddBooks(self):
        domore = 1
        while(domore==1):
            BookName = input("Enter the Name of the Books You Want to Donate Us\n->>> ")
            self.BookList.append(BookName)
            print("\n\t\t\t********Thankyou for your Donation********")
            more = input("\n Want to add more Book? [y/n] = ")
            if(more.lower()== "y"):
                domore = 1
            elif(more.lower()== "n"):
                domore = 0

    def LendBooks(self, BookOwned):
        domore = 1
        nameofperson = input("Enter Your Name ->>> ")
        while (domore == 1):
            nameofbook = input("Enter Your Name of Book You want to Issue ->>> ")
            if(nameofbook in self.BookList):
                BookOwned.update({nameofbook : nameofperson})
                self.BookList.remove(nameofbook)
                print("\n\t\t\t****** Book Allocated Successfully !!! :) ********")
            elif(nameofbook in BookOwned):
                print(f"BOOK IS NOT AVAILABLE, {nameofbook} IS LENDED BY **({BookOwned.get(nameofbook)})** \n Try with at other book")
            else:
                print("Book Is Not available in Library")
            more = input("\n Want to Lend more Book? [y/n] = ")
            if (more.lower() == "y"):
                domore = 1
            elif (more.lower() == "n"):
                domore = 0

    def ReturnBooks(self):
        nameofbook = input("Enter Your Name of Book You want to Submit ->>> ")
        if(nameofbook in BookOwned):
            print(f"Hello, {BookOwned.get(nameofbook)} ")
            self.BookList.append(nameofbook)
            del BookOwned[nameofbook]
            print("\n\t\t\t****** Book Returned Successfully, Thankyou :) ********")
        else:
            print("Book Does not match | it is not a Valid Book OR not Lended to Anyone")



if __name__ == '__main__':
    list_of_books = ["blackhole", "galaxy", "inter plantery life"]
    BookOwned = {}
    KetanLibrary = Library(list_of_books, "KetanLibrary")
    while(1):

        operation = int(input("\n\n\n1. Display Available Books \n2. Add Books, \n3. Lend Books, \n4. Return Books \n\nEnter the Operation you want to Perform \n\n ->>> "))
        if(operation == 1):
            KetanLibrary.DisplayBooks()
        elif(operation == 2):
            KetanLibrary.AddBooks()
        elif(operation == 3):
            KetanLibrary.LendBooks(BookOwned)
        elif(operation == 4):
            KetanLibrary.ReturnBooks()
