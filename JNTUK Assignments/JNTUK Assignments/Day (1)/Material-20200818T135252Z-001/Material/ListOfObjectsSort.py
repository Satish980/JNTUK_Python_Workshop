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
list1.append( Employee("ccc", 52) )

list1.sort(key=lambda x: x.empid)

for obj in list1:
    obj.met()
    #print( obj.name, obj.roll, sep =' ' )

