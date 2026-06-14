#doing linear search in python
mylist=[2,5,7,4,8]
target=7

for i in range(len(mylist)):
    #length of the list is calculated using len() function 
    #i represents the index of the list
    if mylist[i]==target:
        print("found at index", i)

        break
    #break is used to exit the loop once the target is found
else:
    print("not found")
