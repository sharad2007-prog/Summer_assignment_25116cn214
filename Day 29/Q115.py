y = ""

while True:
    print("1.add")
    print("2.uppercase")
    print("3.lowercase")
    print("4.length")
    print("5.reverse")
    print("6.display")
    print("7.exit")

    x = int(input("enter your choice"))

    if x == 1:
        y = input("enter the string")
        print("string has been added successfully")

    elif x == 2:
        if y != "":
            print(y.upper())
        else:
            print("No string found")

    elif x == 3:
        if y != "":
            print(y.lower())
        else:
            print("No string found")

    elif x == 4:
        if y != "":
            print("The length of string is =", len(y))
        else:
            print("No string found")

    elif x == 5:
        if y != "":
            print("The reverse of string is =", y[::-1])
        else:
            print("No string found")

    elif x == 6:
        if y != "":
            print(y)
        else:
            print("No string found")

    elif x == 7:
        print("You have exited")
        break

    else:
        print("Invalid Choice")
