x = input("Enter a string: ")

result = ""
count = 1

for i in range(len(x) - 1):
    if x[i] == x[i + 1]:
        count += 1
    else:
        result += x[i] + str(count)
        count = 1

result += x[-1] + str(count)

print("Compressed string:", result)
