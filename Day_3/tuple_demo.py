#!/usr/bin/python

# tuples in python

atup = ('physics','chemistry',2010,2014)
btup = (80,82,73,64,85)

# to print complete tuple
print("atup :", atup)
print("btup :", btup)

# to print first element of the tuple
print("atup[0]:", atup[0])

# to print elements starting from 2nd till 3rd
print("btup[1:3] : ", btup[1:3])

print("Value available at index 2 :")
print(atup[2])

#Not valid action to the tuple
# atup[2] = 2011

# Instead of assign create a new variable

ctup = atup[0:1] + btup[1:3]

print("New tuple : ")
print(ctup)

# Removing individual tuple elements is not possible
# del atup[2]

del(atup)
print("Tuple Deleted")

# the total length of the tuple
print("Second tuple length : ", len(btup))

#return items from the tuple with max value
print("Max value element :", max(btup))

#return items from the tuple with min value
print("Min value element :", min(btup))

# to converts a tuple into list
tup = ( 2014,'chemistry',84,'Grade B')
listtup = list(tup)
print("List elements :", listtup)