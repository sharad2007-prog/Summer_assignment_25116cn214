#converting lower cqse to uppercase

x = input("Enter your string here: ")

result = ""

for ch in x:
    if ch.islower():
        result += ch.upper()
    else:
        result += ch

print(result)
