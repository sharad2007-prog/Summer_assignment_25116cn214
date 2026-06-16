#to find pair with given sum
arr=[2,7,11,15]
target=9
#we use i=0,j=1 as index position
for i in range(len(arr)):
     for j in range(i+1,len(arr)):
         if arr[i]+arr[j]==target:
            print(arr[i],arr[j]) 
