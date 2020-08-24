


alist = [10,20,30,40,565443,4,400,54,10]



alist.append(600)
print("List elements are :", alist)
alist.append(45)
alist.append(89)
print("List elements are :", alist)

alist.extend([50,34,4,6,45])

print("List elements are :", alist)

print(alist.count(10))

# list.insert(where to insert, what to insert)
alist.insert(0,5)
print("List elements are :", alist)

alist.insert(2,200)
print("List elements are :", alist)

alist.pop()    # by deault last element will be removed
print("List elements are :", alist)
alist.pop(1)    
print("List elements are :", alist)

## we pass the value DIRECTLY ... not the index
alist.remove(200)    # element is passed directly
print("List elements are :", alist)

alist.reverse()
print("List elements are :", alist)

alist.sort()
print("List elements are :", alist)


alist.remove()