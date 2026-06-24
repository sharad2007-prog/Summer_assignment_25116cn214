#checking rotation of string
x = input("Enter first string: ")
y = input("Enter second string: ")

if len(x) == len(y) and y in (x + x):
    print("Strings are rotations of each other.")
else:
    print("Strings are not rotations of each other.")
