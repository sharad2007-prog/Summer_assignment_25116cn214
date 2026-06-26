arr1 = [1, 2, 4, 7]
arr2 = [3, 5, 6, 8]

i = j = 0
arr3 = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        arr3.append(arr1[i])
        i += 1
    else:
        arr3.append(arr2[j])
        j += 1

while i < len(arr1):
    arr3.append(arr1[i])
    i += 1

while j < len(arr2):
    arr3.append(arr2[j])
    j += 1

print(arr3)
