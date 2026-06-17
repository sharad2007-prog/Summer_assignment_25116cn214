#union of two arrays
arr1=[1,2,3,4]
arr2=[3,4,5,6]

union=arr1.copy()

for i in arr2:
   if i not in union:
      union.append(i)

print(union)
  
