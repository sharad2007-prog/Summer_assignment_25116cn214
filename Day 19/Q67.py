# Original matrix
A = [[1, 2, 3],
     [4, 5, 6]]

# Transpose using list comprehension
T = [[A[i][j] for i in range(len(A))]
     for j in range(len(A[0]))]

print("Transpose Matrix:")
for row in T:
    print(row)
