books=[]
status=[]

print("welcome to the library")

while True:
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
    
    x=int(input("enter your choice"))
    
    if x==1:
        book_name=input("enter book name")
       
        
        books.append(book_name)
        status.append("available")
        
        print("book has been added succesfully")
        
    elif x==2:
        for i in range(len(books)):
         print("Book:", books[i])
         print("Status:", status[i])
    
    elif x==3:
        found=False
        y=input("enter your book name")
        for i in range(len(books)):
            if y==books[i]:
                found=True
                break;
        
        if found:
            print(books[i])
            print(status[i])
        else:
            print("no book found")
                
    elif x==4:
        found=False
        y=input("enter your book name to be issued")
        for i in range(len(books)):
            if y==books[i]:
                status[i]="issued"
                found=True
                break;
        if found:
                print(status[i])
        else:
                print("no book found")
                
    elif x==5:
        found = False
        y=input("enter the book to return")
        for i in range(len(books)):
          if y == books[i]:
           status[i] = "available"
           found = True
           print("Book returned successfully")
           break

        if found == False:
            print("No book found")
        
    elif x==6:
        print("exit")
        break;
        
    else:
        print("invalid choice")
