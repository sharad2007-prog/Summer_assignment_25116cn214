employee_ids = []
employee_names = []
employee_salaries = []

print("Welcome to Employee Management System")

while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        emp_name = input("Enter Employee Name: ")
        emp_salary = int(input("Enter Employee Salary: "))

        employee_ids.append(emp_id)
        employee_names.append(emp_name)
        employee_salaries.append(emp_salary)

        print("Employee added successfully.")

    elif choice == 2:
        if len(employee_ids) == 0:
            print("No employee records found.")
        else:
            for i in range(len(employee_ids)):
                print("\nEmployee ID:", employee_ids[i])
                print("Employee Name:", employee_names[i])
                print("Employee Salary:", employee_salaries[i])

    elif choice == 3:
        search = int(input("Enter Employee ID to search: "))
        found = False

        for i in range(len(employee_ids)):
            if search == employee_ids[i]:
                found = True
                print("\nEmployee Found")
                print("Employee ID:", employee_ids[i])
                print("Employee Name:", employee_names[i])
                print("Employee Salary:", employee_salaries[i])
                break

        if found == False:
            print("Employee not found.")

    elif choice == 4:
        update = int(input("Enter Employee ID to update salary: "))
        found = False

        for i in range(len(employee_ids)):
            if update == employee_ids[i]:
                new_salary = int(input("Enter New Salary: "))
                employee_salaries[i] = new_salary
                found = True
                print("Salary updated successfully.")
                break

        if found == False:
            print("Employee not found.")

    elif choice == 5:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice.")
