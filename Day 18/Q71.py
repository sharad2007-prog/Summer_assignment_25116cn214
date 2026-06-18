#binary seach
arr = [1, 2, 3, 4, 5]
x = 4
less = 0
high = len(arr) - 1

while less <= high:
    mid = (less + high) // 2
#middle number=(lowest num.+highest num.)/2
    if arr[mid] == x:
        print("Found")
        break
    elif arr[mid] < x:
        less = mid + 1
    else:
        high = mid - 1
