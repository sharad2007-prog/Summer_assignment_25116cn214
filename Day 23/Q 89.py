#finding first non repeating number
x = input("Enter a string: ")

for ch in x:
    if x.count(ch) == 1:
        print("First non-repeating character is:", ch)
        break
else:
    print("No non-repeating character found.")
