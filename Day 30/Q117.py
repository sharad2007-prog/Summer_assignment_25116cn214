names=[]
marks=[]

while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")
    
    x=int(input("enter your choice"))
    
    if x==1:
        name=input("enter your name")
        mark=int(input("enter your marks"))
        
        names.append(name)
        marks.append(mark)
        
        print("student has been succesfuy added")
        
    elif x==2:
       print(names)
       print(marks)
       
    elif x==3:
        found=False
        search=input("enter the name to search")
        for i in range(len(names)):
            if search==names[i]:
                found=True
                break;
        if found:
            print(names[i])
            print(marks[i])
        else:
            print ("no student found")
            
    elif x==4:
        print("exited")
        break;
        
    else:
        print("invaild choice")
