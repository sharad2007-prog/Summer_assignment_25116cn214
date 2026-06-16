#removing duplicates from an array
arr=[1,2,2,3,4,4,5] 
x=[]
for i in range(len(arr)):
  
      if arr[i] not in x:
          x.append(arr[i])
       
print(x)
        
