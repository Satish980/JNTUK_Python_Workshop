

# In python2.x  raw_input()

name = input("Enter any name :")
print(name)

# input ONLY understands STRING
first = int(input("Enter first value :"))
second = input("Enter second value :")

total = int(first) + int(second)
print("sum of numbers :", total)

alist =[10,20,30,40]

print(max(alist))
print(min(alist))
print(sum(alist))

atup = (10,20,30,40)
#atup[0] = 10
alist = list(atup)     # converting to the list
alist[0] = 1000
atup = tuple(alist)    # reconverting back to tuple
print(atup)


name = "python"
print(type(name))

print(isinstance(name,list))  # will return True or False

alist =[10,20,30,40]
print(isinstance(alist,list))


alist = [10,20,30,40,43]
print(len(alist))





