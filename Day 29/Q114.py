arr=[]

while True:
    print("1.insert number")
    print("2.display number")
    print("3.search number")
    print("4.delete number")
    print("5.exit")
    
    choice=int(input("enter your choice"))
    if choice ==1:
        y=int(input("enter the number to add in array"))
        arr.append(y)
        print("number has been added succesfully")
        
    elif choice==2:
        print(arr)

    elif choice==3:
        found=False
        y=int(input("enter the number to search in array"))
        for num in arr:
            if num==y:
                found=True
                
        if found:   
                print("number is presnt")
                
        else:
                print("number is not present")
                
    elif choice ==4:
        found=False
        y=int(input("enter the number to remove in array"))
        for num in arr:
         if num==y:
            found=True 
            arr.remove(y)
            
        if found:    
            print("number has been removed succesfully")
        else:
            print("number is not found in array")
            
    elif choice==5:
        print("you have been exit ")
        break;
        
    else:
        print("invalid choice")
