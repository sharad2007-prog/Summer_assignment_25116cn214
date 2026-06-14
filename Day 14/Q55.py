#finding second largest element in a list
mylist=[12,45,7,34,45]

mylist.sort(reverse=True)
#sort(reverse=True) method is used to sort the list in descending order

print("second largest number is", mylist[1])
#here mylist[1] is used to access the second largest element in the sorted list 
