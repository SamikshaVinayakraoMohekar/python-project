# print("Crude operatin in OOP")

class Book:
    def __init__(self):
        self.books = {}
        self.book = {
            'title': '',
            'author':'',
            'Published_year':'',
            'price':''  
        }
        
    def Choice_opr(self):
        
        while True:
            print('''
            1: Create Book
            2: Read book
            3: Update book
            4: Delete book
            ''')
            ch=int(input("Enter the choice:= "))
            
            if ch==1:
                self.Create_book()
            elif ch==2:
                self.Read_books()
            elif ch==3:
                self.Update_book()
            elif ch==4:
                self.Delete_book()
            else:
                print("Invalid choice")
                ch=int(input("Please enter Re-enter the choice:= "))


    def Create_book(self):
        print("Add a Book")

        title=input("Enter the title of book: ")
        self.book['title']=title

        author=input("Enter the name of author: ")
        self.book['author']=author

        published_year=int(input("Enter the year when book published: "))
        self.book['published_year']=published_year

        price=int(input("Enter the price of book:"))
        self.book['price']=price

        book_code=int(input("Enter the book code: "))
        self.books[book_code]=self.book

        print(f"Book {book_code} is created sucessfully")


         
    def Read_books(self):
        print("#----Reading book---#")
        for k,v in self.books.items():
            print(k,end="\t")
            for b in v.values():
                print(b,end="\t")
            print("\n")
        print("\n")


    def Update_book(self):
        print("Updating the book")
        book_code=int(input("Enter the book code for editing: "))
        if book_code in self.books:
            while True:
                ch_ed=int(input("Enter the choice for editing: "))
                print('''
                    1: title,
                    2: author,
                    3: published_year,
                    4: price,
                    5: book code
                    6: 
                      
                ''')
                if ch_ed==1:
                    title=input("Enter the title of book: ")
                    self.books[book_code]['title']= title
                elif ch_ed==2:
                    author=input("Enter the author name: ")
                    self.books[book_code]['author']= author
                elif ch_ed==3:
                    published_year=int(input("Enter the published-year"))
                    self.books[book_code]['published_year']=published_year
                elif ch_ed==4:
                    price=int(input("Enter the price of book:"))
                    self.books[book_code]['price']=price
                elif ch_ed==5:
                    book_code=int(input("Enter the book code:"))
                    self.books[book_code]=book_code
                elif ch_ed==6:
                    self.Choice_opr()
                else:
                    print("Invalide choice for editing")

        
        else:
            print("you provided wrong book-code")
            self.Choice_opr()



    
    def Delete_book(self):
        print("Deleting  book")
        book_code=int(input("Enter the book-code:"))

        if book_code in self.books:
            del self.books[book_code]
            print(f"Book code {book_code} is deleted sucessfully")
        else:
            print(" you entered the wrong book code!")



obj=Book()
print(obj.Choice_opr())

    
