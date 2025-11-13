from datetime import datetime, timedelta 
#this lets me set a due date
library_books = [
    {
        "id": "B1",
        "title": "The Lightning Thief",
        "author": "Rick Riordan",
        "genre": "Fantasy",
        "available": True,
        "due_date": None,
        "checkouts": 2
    },
    {
        "id": "B2",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Historical",
        "available": False,
        "due_date": "2025-11-01",
        "checkouts": 5
    },
    {
        "id": "B3",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "available": True,
        "due_date": None,
        "checkouts": 3
    },
    {
        "id": "B4",
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "available": True,
        "due_date": None,
        "checkouts": 4
    },
    {
        "id": "B5",
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "available": True,
        "due_date": None,
        "checkouts": 6
    },
    {
        "id": "B6",
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "available": False,
        "due_date": "2025-11-10",
        "checkouts": 8
    },
    {
        "id": "B7",
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "genre": "Science Fiction",
        "available": True,
        "due_date": None,
        "checkouts": 1
    },
    {
        "id": "B8",
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-Age",
        "available": False,
        "due_date": "2025-11-12",
        "checkouts": 3
    }
]
#This is a function that shows all the books in the catalog   
def availablebooks(library_books) :
    for book in library_books : #this loops through each book
        if book ["available"] == True : #this checks what "available" says on the book
            status = "available" #declaring a variable with the value of available so I can print it later
            print(book["id"], "-",book["title"], "-",book["author"], "-",book["genre"], "|", status) 
        else:
            status = "Checked out"
        print(book["id"], "-",book["title"], "-",book["author"], "-",book["genre"], "|", status) 
    starttheprogram(library_books)

#This is a function that allows the user to search for a book
def search_books(library_books) :
    found = False  #declaring a variable allows me to check for the books that are available, and filters out the unavailable books
    userchoice = input("What author or genre are you searching for? :").lower()
    for book in library_books : #again looping through each book in the library
        if book["author"].lower() == userchoice or book["genre"].lower() == userchoice : #using or lets the user search either using the author or genre
           
           print(book["id"], "-", book["title"], "-", book["author"], "-", book["genre"])
           found = True #making found true lets the system know that the book is available
    starttheprogram(library_books)

    if found == False :
        print("Book not found.") #if the book is assigned found = false, it wont print it. 
        starttheprogram(library_books)

def checkout_book(library_books) :
    foundID = False #same logic as function search_books
    checkout_book_user = input("Enter the book ID you would like to checkout. : ")
    for book in library_books :
        if book["id"].lower() == checkout_book_user.lower() : #makes the input case insensitive
          foundID = True
          if book["available"] == True : #if the book is available, it will do the following
             book_status = book["available"]
             print(book["id"], "-", book["title"], "-", book["author"], "-", book["genre"],"-", book["available"], "-", book["due_date"], "-", book["checkouts"])
             print("You are checked out!")
             book["available"] = False #this sets the available of the book to false since they are checking it out
             book["checkouts"] += 1 #adds one more checkout to the book
             book["due_date"] = datetime.now() +timedelta(weeks=2) #this sets the due date from 2 weeks from now
             starttheprogram(library_books)
          else :
             print("The book isn't available.")
             starttheprogram(library_books)
        
    if foundID == False :
             print("The book ID is not valid") #the variable checks if the ID is valid or not

def return_book(library_books) :
    return_user = input("What book would you like to return? : ")
    returnID = False #same idea as search_books
    for book in library_books :
        if book["id"].lower() == return_user.lower() : #makes sure the input is case insensitive
            returnID = True
            book["available"] = True #since the user is returning the book, the book is now available
            book["due_date"] = None #resets the due date
            print("Successfully returned book!")
            print(book["id"], "-", book["title"], "-", book["author"], "-", book["genre"],"-", book["available"], "-", book["due_date"], "-", book["checkouts"])
            starttheprogram(library_books)
            for book in library_books :
                if book["due_date"] > datetime.now() :
                    print("Additionally, the following books are due.")
                    print(book["id"], "-", book["title"], "-", book["author"], "-", book["genre"],"-", book["available"], "-", book["due_date"], "-", book["checkouts"])
        else :
            userinput = input("Invalid Id, Please try again!").lower()
            starttheprogram(library_books)

def starttheprogram(library_books) :
    userinput = input("Type 1 to access the book libary catalog, type 2 to search by an author or genre, type 3 to check out a book and type 4 to return a book. Type 5 to close the application.   :     ")
    print(userinput)
    if userinput == "1" :
        availablebooks(library_books)
    elif userinput == "2" :
        search_books(library_books)
    elif userinput == "3" :
        checkout_book(library_books)
    elif userinput == "4" :
        return_book(library_books)
    elif userinput == "5" :
        print("Thank you! Have a good day!")
    else : 
        userinput = input("Incorrect input, Please enter 0 and re-enter JUST the integer you would like to view.  :  ")
        starttheprogram(library_books)
starttheprogram(library_books)