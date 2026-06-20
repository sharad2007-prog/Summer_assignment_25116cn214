A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for j in range(len(A[0])):   # Loop through columns
    col_sum = 0
    for i in range(len(A)):  # Loop through rows
        col_sum += A[i][j]
    print("Sum of column", j + 1, "=", col_sum)
