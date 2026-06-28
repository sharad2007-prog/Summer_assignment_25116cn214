print("welcome to library management")

books=[]

while True:
 print("1. Add Book")
 print("2. Search Book")
 print("3. Issue Book")
 print("4. Return Book")
 print("5. Exit")
 
 x=int(input("enter your choice")  )
 
 if x==1:
    book_id=int(input("enter your book id")) 
    book_name=input("enter your book name")
    book_author=input("enter your author name")
    book_qty=int(input("enter the book qty"))
    
     
    book= {
     "book_id;":book_id,
     "book_name;":book_name,
     "book_author;":book_author,
     "book_qty;":book_qty
         }
         
    books.append(book) 
    print("book has been added")
    
 elif x==2:
     y=int(input("enter your book id to search"))
     for book in books:
      if book["book_id;"]==y:
         print("book_id;",book["book_id;"])
         print("book_name;",book["book_name;"])
         print("book_author;",book["book_author;"])
         print("book_qty;",book["book_qty;"])
         
         print("book has been found")
         break;
         
 elif x==3:
      z=int(input("enter your book id to issue the book"))
      for book in books:
        if book["book_id;"]==z:
         print("book_id;",book["book_id;"])
         print("book_name;",book["book_name;"])
         print("book_author;",book["book_author;"])
         print("book_qty;",book["book_qty;"])  
            
            
         if book["book_qty;"]>0:
             book_qty=book_qty-1
             print("book has been issue",)
             print("remaining book qty is;",book_qty)
         else:
             print("no books remain")
         break;
         
 elif x==4:
      u=int(input("enter your book id to return the book"))
      for book in books:
        if book["book_id;"]==u:
         print("book_id;",book["book_id;"])
         print("book_name;",book["book_name;"])
         print("book_author;",book["book_author;"])
         print("book_qty;",book["book_qty;"])  
            
            
         
        book_qty=book_qty+1
        print("book has been returned",)
        print("new book qty is;",book_qty)
             
 elif x==5 :
     print("you have been exit")
     break;
