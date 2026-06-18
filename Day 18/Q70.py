#selection sort 
arr = [5, 3, 8, 4, 2]
for i in range(len(arr)):
    smallest = i

    for j in range(i + 1, len(arr)):
        if arr[j] < arr[smallest]:
            smallest = j

    arr[i], arr[smallest] = arr[smallest], arr[i]
print(arr)
