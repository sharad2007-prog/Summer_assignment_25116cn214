3finding first multi repeating character
x = input("Enter a string: ")

for ch in x:
    if x.count(ch) > 1:
        print("First repeating character is:", ch)
        break
else:
    print("No repeating character found.")
