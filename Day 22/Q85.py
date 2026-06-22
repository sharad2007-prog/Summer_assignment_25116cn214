# Input string from user
text = input("Enter a string: ")

# Reverse the string using slicing
reverse_text = text[::-1]

# Compare original and reversed strings
if text == reverse_text:
    print("Palindrome String")
else:
    print("Not a Palindrome String")
