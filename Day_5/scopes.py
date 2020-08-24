

value = 1 # global variable

def displayValue():
    print(value)

displayValue()


##################################################################
#need to modify the global variable from inside a function.
##################################################################
value = 1 # global variable   
def displayValue():
    value = value + 2 # increment c by 2
    print(value)

displayValue()



##################################################################
#Changing Global Variable From Inside a Function using global
##################################################################
value = 0 # global variable

def displayValue():
    global value
    value = value + 2 # increment by 2
    print("Inside add():", value)

displayValue()
print("In main:", value)


##################################################################

x = "python programming"

def displayInfo():
    print("x inside:", x)

displayInfo()
print("x outside:", x)


##################################################################
######## local variable
#A variable declared inside the function's body or 
#in the local scope is known as a local variable.
##################################################################
def displayData():
    y = "local"

displayData()
print(y)



##################################################################
# accessing global and local variables
##################################################################
x = "this is global object"

def displayName():
    global x
    y = "this is local object"
    x = x * 2
    print(x)
    print(y)

displayName()

##################################################################
#Global variable and Local variable with same name
##################################################################
x = 5

def displayOutput():
    x = 10  #local scope
    print("local x:", x)

displayOutput()
print("global x:", x)









#Nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.

def checkOutput():
    x = "local"

    def innerOutput():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    innerOutput()
    print("outer:", x)

checkOutput()




