#row wise sum
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(A)):
    row_sum = 0
    for j in range(len(A[0])):
        row_sum += A[i][j]
    print("Sum of row", i + 1, "=", row_sum)
