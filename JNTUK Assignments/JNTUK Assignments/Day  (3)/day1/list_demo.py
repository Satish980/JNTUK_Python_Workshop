#!/usr/bin/python

alist = ['physics','chemistry',2010,2014]
markslist = [ 80,82,73,64,85]

# to print complete list
print("alist : ", alist)
print("markslist : ",markslist)
print()

# to print first element of the list
print("alist[0] :", alist[0] )
print()

# to print elements starting from 2nd up to 3rd element
print("makslist[1:3]:", markslist[1:3])
print()

print("Value available at index 2 : ")
print(alist[2])
print()

#assign to the list

alist[2] = 2011

print("New value available at index 2 : ")
print(alist[2])

print(alist)
print()

# deleting value at particular index
del(alist[2])

print("First list length after deletion: ", len(alist))
print("After deleting value :")
print(alist)
print()

#return items from the list with max value
print("Max value element : ", max(markslist))
print()

#return items from the list with min value
print("min value element : ", min(markslist))
print()
