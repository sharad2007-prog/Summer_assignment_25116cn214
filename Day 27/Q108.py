print("===== Marksheet Generation System =====")

name = input("Enter Student Name: ")
roll = int(input("Enter Roll Number: "))

m1 = float(input("Enter Marks of Subject 1: "))
m2 = float(input("Enter Marks of Subject 2: "))
m3 = float(input("Enter Marks of Subject 3: "))
m4 = float(input("Enter Marks of Subject 4: "))
m5 = float(input("Enter Marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if m1 >= 33 and m2 >= 33 and m3 >= 33 and m4 >= 33 and m5 >= 33:
    result = "PASS"
else:
    result = "FAIL"

print("\n========== MARKSHEET ==========")
print("Student Name :", name)
print("Roll Number  :", roll)
print("Subject 1    :", m1)
print("Subject 2    :", m2)
print("Subject 3    :", m3)
print("Subject 4    :", m4)
print("Subject 5    :", m5)
print("-------------------------------")
print("Total Marks  :", total, "/500")
print("Percentage   :", percentage, "%")
print("Grade        :", grade)
print("Result       :", result)
print("===============================")
