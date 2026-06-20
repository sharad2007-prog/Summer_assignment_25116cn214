#sum  of diagonal
A = [
    [1, 2],
    [3, 4]
]

sum = 0

for i in range(len(A)):
    sum = sum + A[i][i]

print(sum)
