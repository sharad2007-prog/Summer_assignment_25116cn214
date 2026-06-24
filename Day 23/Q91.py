#checking anagram strings or numbers 
x = input("Enter first string: ")
y = input("Enter second string: ")

if sorted(x) == sorted(y):
    print("Strings are Anagrams")
else:
    print("Strings are not Anagrams")
