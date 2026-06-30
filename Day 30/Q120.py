names = []
marks = []

def add_student():
    name = input("Enter student name: ")
    mark = int(input("Enter student marks: "))

    names.append(name)
    marks.append(mark)

    print("Student added successfully.")

def display_students():
    if len(names) == 0:
        print("No students found.")
    else:
        for i in range(len(names)):
            print("Name:", names[i])
            print("Marks:", marks[i])
            print()

def search_student():
    search = input("Enter student name: ")
    found = False

    for i in range(len(names)):
        if search == names[i]:
            print("Name:", names[i])
            print("Marks:", marks[i])
            found = True
            break

    if found == False:
        print("Student not found.")

def update_marks():
    search = input("Enter student name: ")

    found = False

    for i in range(len(names)):
        if search == names[i]:
            new_marks = int(input("Enter new marks: "))
            marks[i] = new_marks
            print("Marks updated successfully.")
            found = True
            break

    if found == False:
        print("Student not found.")

def main():

    while True:

        print("\n----- Student Management System -----")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_marks()

        elif choice == 5:
            print("Thank You")
            break

        else:
            print("Invalid Choice")

main()
