

alist = [10,20,30,40]
#output: [15,25,35,45]
blist = []
for val in alist:
    blist.append(val + 5)
print(blist)


alist = [10,20,30,40]
for val in alist:
    index = alist.index(val)
    alist[index] = val + 5
print(alist)


# list comprehsion
alist = [10,20,30,40]
blist = [  val + 5    for val in alist]
           ## 2nd###  #### 1st ####
print(blist)


#map() : if some operation has to be applied for all the elements in list, then map is used
alist = [10,20,30,40]
def increment(x):
    return x + 5
# map(function,iterable)
print(list(map(increment,alist)))


names = ["unix","linux","spark","machinelearning"]
def getUpper(name):
    return name.upper()

print(list(map(getUpper,names)))


print(list(map(lambda x:x.upper(),names)))


# display all odd numbers
alist = [10,20,30,40,5,5,4,3,5,6,4,432,43]
for val in alist:
    if val %2 == 1:
        print(val)


alist = [10,20,30,40,5,5,4,3,5,6,4,432,43]
print(list(filter(lambda x: x %2 ,alist)))































