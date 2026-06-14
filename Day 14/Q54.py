#finding frequency of an element in a list
mylist=[7,2,7,4,7,1]
target=7
count=0 
#here count =0 for initially count is 0 
for i in range(len(mylist)):
    if mylist[i]==target:
      count=count +1
# here space is given to print for the print to be off the loop and print the frequency only
print("frequency of", target, "is", count)
