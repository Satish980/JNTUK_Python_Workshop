#List of employee objects
class Employee:
    def __init__(self, name, empid):
        self.name = name
        self.empid = empid
        print("This is Employee constructor")

    def met(self):
        print("This is met in Employee class"+str(self.empid))


# creating list
list1 = []

# appending instances to list
list1.append( Employee("aaaa", 200) )
list1.append( Employee("bbbb", 26) )
list1.append( Employee("cccc", 52) )
print("\n")
for obj in list1:
    obj.met()
    #print( obj.name, obj.roll, sep =' ' )

#another compact way of pritning a list
print([item.name for item in list1])

