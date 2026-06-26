#making quiz program
print("welcome to quiz")

score=0

print("What is the capital of India?")
print("1. Mumbai")
print("2. Delhi")
print("3. Chennai")
print("4. Jaipur")
x=int(input("enter your choice"))

if x==2:
    score=score+1
    print("correct answer")
else:
    print("incorrrect answer")
    
print("score",score)    
    
print("What is 10 × 5?")
print("1. 20")
print("2. 45")
print("3. 15")
print("4. 50")
x=int(input("enter your choice"))

if x==4:
    score=score+1
    print("correct answer")
else:
    print("incorrrect answer")
    
print("score",score)

print("Which language are you learning?")
print("1. python")
print("2. java")
print("3. c++")
print("4. c")
x=int(input("enter your choice"))

if x==1:
    score=score+1
    print("correct answer")
else:
    print("incorrrect answer")
    
print("score",score)

print("your score is:",score)
