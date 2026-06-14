#finding duplicate elements in a array/list
mylist=[2,5,7,4,8,5,7]
duplicates=[]
#we use two pinters i and j 
#we set i=o index and j=1 index
for i in range(len(mylist)):
    
    for j in range(i+1, len(mylist)):
        if mylist[i] == mylist[j]:
            #
            duplicates.append(mylist[i])
            #append() method is used to add the duplicate element to the duplicates list
print("duplicates:", duplicates)
