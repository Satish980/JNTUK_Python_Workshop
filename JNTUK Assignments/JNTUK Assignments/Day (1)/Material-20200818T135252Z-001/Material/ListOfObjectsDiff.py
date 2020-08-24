#List of employee objects
class Employee:
    def __init__(self, name, empid):
        self.name = name
        self.empid = empid
        print("This is Employee constructor")

    def met(self):
        print("This is met in Employee class"+str(self.empid))

    def __hash__(self):
        return hash((self.empid, self.name))

    def __eq__(self, obj):
        return isinstance(obj, Employee) and obj.empid == self.empid

    def __ne__(self, other):
        return not self == obj


# creating list
list1 = []

# appending instances to list
list1.append( Employee("aaaa", 200) )
list1.append( Employee("cccc", 52) )
list1.append( Employee("bbbb", 26) )
list1.append( Employee("cccc", 52) )

sobjs = set(list1)
print("\n")
for obj in sobjs:
    obj.met()
    #print( obj.name, obj.roll, sep =' ' )

#another compact way of pritning a list
print([item.name for item in sobjs])

print("-------------------------------------\n")
list2 = [ Employee("aaaa", 200) , Employee("cccc", 52) ]
list3 = list1-list2
print([item.name for item in list3])

