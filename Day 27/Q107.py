employees = []

while True:
    print("\n===== Salary Management System =====")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))

        employee = {
            "id": emp_id,
            "name": name,
            "salary": salary
        }

        employees.append(employee)
        print("Employee added successfully!")

    elif choice == 2:
        if len(employees) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records")
            for employee in employees:
                print("----------------------")
                print("ID     :", employee["id"])
                print("Name   :", employee["name"])
                print("Salary :", employee["salary"])

    elif choice == 3:
        emp_id = int(input("Enter Employee ID to search: "))
        found = False

        for employee in employees:
            if employee["id"] == emp_id:
                print("\nEmployee Found")
                print("ID     :", employee["id"])
                print("Name   :", employee["name"])
                print("Salary :", employee["salary"])
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == 4:
        emp_id = int(input("Enter Employee ID to update salary: "))
        found = False

        for employee in employees:
            if employee["id"] == emp_id:
                new_salary = float(input("Enter New Salary: "))
                employee["salary"] = new_salary
                print("Salary updated successfully!")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == 5:
        emp_id = int(input("Enter Employee ID to delete: "))
        found = False

        for employee in employees:
            if employee["id"] == emp_id:
                employees.remove(employee)
                print("Employee deleted successfully!")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid choice! Please try again.")
