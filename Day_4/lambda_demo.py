#!/usr/bin/python

# Anonymous Functions Lambda
print("Example Program1 - Anonymous function lambda:\n")
total = lambda sub1,sub2,sub3,sub4,sub5: sub1 + sub2 + sub3 + sub4 + sub5

# Now you can call total as a function
print("Student1 marks of total : ", total(70,80,90,80,85))
print("Student2 marks of total : ", total(90,85,95,85,95))

# Pass by assignment
# Function definition is here
def func_ref( list ):
    print("List values inside the function before append : ", list)
    # to change a passed list into function
    list.append([90,75,68,84])
    print("List values inside the function after append:", list)
    return


# Now you can call user defined function
list = [60,70,80]
print("Example Program - 2 : Pass assignment\n")
print("List values before calling the function:", list)

# To call the function
func_ref(list)
print("List values outside the function :", list )
#########################################################
# Pass by value
# Function definition is here
def func_value ( obj ) :
    # To change a passed parameter into function
    obj = 90 # assigning new reference to obj
    print("Values inside the function: ", obj)
    return

# Now you can call userdefined function
print("Example program 3 - Pass by value\n")
obj = 80
print("Values before calling the function: ", obj )
func_value(obj)
print("Values outside the function:", obj )
