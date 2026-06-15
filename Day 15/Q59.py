#rotating an array rightwards
arr=[3,4,5,1,2]

last=arr[-1]
#-1 represents the negative slicing
arr=arr[:-1]
arr.insert(0,last)
#.insert is used to insert the elements 
print(arr)
