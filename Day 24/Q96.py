x = input("Enter a string: ")

result = ""

for ch in x:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)
