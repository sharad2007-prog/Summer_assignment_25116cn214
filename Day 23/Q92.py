x = input("Enter a string: ")

max_char = x[0]
max_count = x.count(x[0])

for ch in x:
    if x.count(ch) > max_count:
        max_count = x.count(ch)
        max_char = ch

print("Maximum occurring character is:", max_char)
print("It occurs", max_count, "times.")
