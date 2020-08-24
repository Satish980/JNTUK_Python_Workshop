
def increment(x):
    return x + 1

total = increment(10)
print(total)


# lambda : lambda in python is single liner function
# syntax : function = lambda variables : expression

increment = lambda x : x + 1

total = increment(10)
print(total)

# reguar way
def getUpper(uname):
    return uname.upper()

name = getUpper("python")
print(name)


# using lambda
getUpper = lambda lang : lang.upper()
name = getUpper("python")
print(name)


# using lambda
add = lambda x,y : x + y
getsum = add(10,20)
print(getsum)











