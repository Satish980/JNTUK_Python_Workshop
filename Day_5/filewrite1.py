


# opening the file
fobj = open("numbers.txt","w")

fobj.write("python programming\n")


# closing the file
fobj.close()



'''
fobj = open(r"D:\test\numbers.txt","w")     # raw string  ## OR
fobj = open("D:\\test\\numbers.txt","w")   ## OR
fobj = open("D:/test/numbers.txt","w")     
'''


# opening the file
fobj = open(r"D:\test\numbers.txt","w")

fobj.write("python programming\n")

# closing the file
fobj.close()



# opening the file  - regular|traditional file
fobj = open(r"D:\test\numbers_all.txt","w")
for val in range(1,11):
    fobj.write(str(val) + "\n")
fobj.close()


# context manager
# It is NOT required close the file
# file gets closed automatically when it comes out of indentation
with open("numbers.txt","w") as fobj:
    for val in range(1,11):
        fobj.write(str(val) + "\n") 


#### 


















