employees=[]

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Delete Employee")
    

    choice = int(input("Enter your choice: "))
    
    if choice==1:
        emp_id=int(input("enter your employee id"))
        name=input("enter your name")
        salary=int(input("enter your salary"))
        
        employee={
            "id":emp_id,
            "name":name,
            "salary":salary
        
        }
        employees.append(employee)
        print("employee has been added")
        
    elif choice==2:
        x=int(input("enter your employee id"))
        for employee in employees:
            if employee["id"]==x:
             
                print("id:",employee["id"])
                print("name:",employee["name"])
                print("salary:",employee["salary"])
            
            print("employee has been found")
                
    elif choice==3:
        x=int(input("enter your employee id"))
        for employee in employees:
            if employee["id"]==x:
             employees.remove(employee)
            print("employee has been removed")           
                
                
                
                
                
                
                
                
                
                
                
                
