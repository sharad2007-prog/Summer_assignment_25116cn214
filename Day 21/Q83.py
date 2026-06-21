#checking and counting vowels and consonants
x = input()

vowel = 0
consonant = 0

for ch in x:
    if ch.isalpha():              # Is it a letter?
        if ch in "aeiouAEIOU":    # Is it a vowel?
            vowel += 1
        else:                     # Otherwise, it's a consonant
            consonant += 1

print(vowel)
print(consonant)
