



alist = [10,20,30,40,50,60,70,56,54,54,5454]
blist = ["oracle","microsoft","unix"]
clist = [10,20,"oracle"]

# assigning new element to the list
alist[0] = 1000
print("after modifying :", alist)



print(alist[0])
print("elements are :", alist)

# slicing
print(alist[0:1])
print(alist[0:3])
print(alist[4:7])
print(alist[-1])
print(alist[::])  # all the values
print(alist[::-1]) # reverse the elements