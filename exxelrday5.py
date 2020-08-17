A = [10,20,40]
print([x+5 for x in A])


names = ["unix","ffdd","os"]

print(list(map(lambda x:x.upper(),names)))



a = [10,20,40,3,2,5,6,7]
print(list(filter(lambda i:i %2 == 0,a)))


f = open("Numbers.txt","w")
for i in range(10):
         f.write(str(i)  + "\n")
f.close()

with open("Numbers.txt","w") as f:
         for val in range(11):
                  f.write(str(val) + "\t")

