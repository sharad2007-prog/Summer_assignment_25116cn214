# subracting two matrices
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))



# Input elements of the first matrix
print("Enter elements of the first matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

# Input elements of the second matrix
print("Enter elements of the second matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    B.append(row)

# Subtract the matrices
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] - B[i][j])
    C.append(row)

)
for row in C:
    print(row)
