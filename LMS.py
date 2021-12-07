# Making a Library blueprint

class Student_Library:

    # Library constructor which takes names of books in a list and name of the library
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}  
        # Book name is key in dictionary which will come from bookList      
        # Dictionary which will be used to fill only those books which are being lend

    
    # Fuction to display all the books
    def displayBooks(self):
        print(f"We have following books in {self.name} :")
        for book in self.bookList:
            print(book)

    # Fuction to see which books are not available to lend
    def displayLendBooks(self):
        # If dictionary is empty, so to avoid any erros
        bool1 = not bool(self.lendDict)
        if bool1:
            print("You can lend any books you want")
        else:
            print("These books are not available right now:")
            # print(self.lendDict.keys())
            for key in self.lendDict:
                print(key)
            
    
    # Fuction to lend the book
    def lendBooks(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lending of book is successfull. Thank you for using our facility")
        else:
            print(f"Book is not available right now. It is currently with {self.lendDict[book]}")

    # Fuction to add new book
    def addBooks(self, book):
        self.bookList.append(book)
        print("Book has been added successfully")

    # Fuction to return the book
    def returnBooks(self, book):
        # Dictonary should not be empty before performing pop
        bool1 = not bool(self.lendDict)
        if bool1:
            print("Invalid option. Please select carefully")

        else:
            self.lendDict.pop(book)
            print("Book has been returned successfully")

        

# Main where actual program will run
if __name__=='__main__':

    book_list = ['Atomic Habits', 'Rich Dadd Poor Dad', 'Harry Potter', 'Lord of the Rings']
    library_name = "Helios_Library"
    library_obj = Student_Library(book_list, library_name)

    # Creating this loop so that user can use the library again without going outside the portal
    while(True):

        #-----------
        # Creating this loop so that user cannot type wrong input and can interact with portal 
        # without worrying of selecting only right options
        program2 = True
        while(program2):

            print(f"\nWelcome to {library_obj.name} : \n")
            print("Press 1 to display books")
            print("Press 2 to display books which are not available right now")
            print("Press 3 to lend books")
            print("Press 4 to add books")
            print("Press 5 to return books")
            print("Press 6 to exit the portal \n")

            user_input1 = input()

            if(user_input1 == '6'):
                print("Thank you for using our portal....")
                exit()

            elif user_input1 not in ['1','2','3','4','5']:
                print("------Please enter a valid input-------")
                # Sending user back to choose between these five options only
                
            else:
                user_input1 = int(user_input1)
                program2 = False
        
        # End of first part where user interaction will be there to start and also the end of while loop

        # Four options is there for the user to use library functions and using if else ladder we can implement those
        
        if(user_input1 == 1):
            library_obj.displayBooks()

        elif(user_input1 == 2):
            library_obj.displayLendBooks()

        elif(user_input1 == 3):
            user = input("Enter your name = ")
            book = input("Enter book name = ")
            library_obj.lendBooks(user, book)

        elif(user_input1 == 4):
            book = input("Enter the name of book you want to add = ")
            library_obj.addBooks(book)

        elif(user_input1 == 5):
            book = input("Enter the name of book you want to return = ")
            library_obj.returnBooks(book)
            

        print("\nPress Q to quit and C to continue ")
        user_input3 = input()
        user_input3 = user_input3.upper()
        if(user_input3 == 'C'):
            continue
        else:
            print("Thank you for using our portal....")
            exit()
        