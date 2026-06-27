students = []

while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll Number")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))

        student = {
            "roll": roll,
            "name": name,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records")
            for student in students:
                print("----------------------")
                print("Roll :", student["roll"])
                print("Name :", student["name"])
                print("Marks:", student["marks"])

    elif choice == 3:
        roll = int(input("Enter Roll Number to search: "))
        found = False

        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found")
                print("Roll :", student["roll"])
                print("Name :", student["name"])
                print("Marks:", student["marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 4:
        roll = int(input("Enter Roll Number to delete: "))
        found = False

        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                print("Student record deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
