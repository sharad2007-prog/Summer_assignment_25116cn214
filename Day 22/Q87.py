# Input string from user
text = input("Enter a string: ")

# Dictionary to store character frequencies
frequency = {}

# Count occurrences of each character
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Display frequencies
print("Character Frequencies:")
for char, count in frequency.items():
    print(char, ":", count)
