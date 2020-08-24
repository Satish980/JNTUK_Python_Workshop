class TDetails:
    def __init__(self, cname, temp):
        self.cname = cname
        self.temp = temp
        print("This is TDetails constructor")

    def __repr__(self):
        return self.cname+"\t"+str(self.temp)

    def __hash__(self):
        return hash((self.cname, self.temp))

    def __eq__(self, obj):
        return isinstance(obj, TDetails) and obj.cname == self.cname

    def __ne__(self, obj):
        return not self == obj

    def met(self):
        print("This is met in TDetails class: "+self.cname+"\t"+str(self.temp))


temps = [TDetails("Kakinada", 32.1), TDetails("Bangalore", 35.2), TDetails("Hyderabad", 31.5)]

#lambda is anonymous function
temps.sort(key=lambda x: x.temp, reverse=True)

for val in temps:
    print(val)
'''
temps1 = temps[:2]

temps2 = temps[-2:]

tempsa = [31.6,40.1,26.8]

print("After sorting: Maximum two temperatures")

for val in temps[-2:]:
    print(val)
'''
#List stores the duplicates and maintains insertion order
temps.append(TDetails("Kakinada", 32.1))
#temps.extend(temps)
stemps = set(temps)

for val in stemps:
    print(val)


