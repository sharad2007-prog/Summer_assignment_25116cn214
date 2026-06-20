#tranpose of matrix
A = [
    [1, 2, 3],
    [4, 5, 6]
]

T = []  # Transposed matrix

# Loop through columns of A
for i in range(len(A[0])):
    row = []

    # Loop through rows of A
    for j in range(len(A)):
        row.append(A[j][i])  # Take element and add to new row

    T.append(row)  # Add row to transpose

print(T)
