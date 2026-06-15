#moving zeroes in the end of the array
arr=[1,0,3,0,5,0,2]

for i in arr:
    if i==0:
     arr.remove(i)
     arr.append(0)
print(arr)
