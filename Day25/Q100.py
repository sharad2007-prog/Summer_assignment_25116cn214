#sorting words on thier length
words = input("Enter words: ").split()

words.sort(key=len)

print("Words sorted by length:")
print(words)
