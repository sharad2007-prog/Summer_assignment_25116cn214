# Input the order of the square matrix
n = int(input("Enter the size of the matrix (n x n): "))

# Input the matrix
matrix = []
print("Enter the elements of the matrix:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)

# Calculate the sum of the principal diagonal
diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix[i][i]

# Display the result
print("Sum of diagonal elements =", diagonal_sum)
