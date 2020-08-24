


# In python , if any object is prefixed with * .... it becomes tuple
# In python, if any object is prefixed with ** ... it becomes dictionary


def display(*numbers):
    for val in numbers:
        print(val)
    
display(10,20,30,40,50,4,4,35,354,3,4,4,3,3,2,2,24,4,"unix",4534,6554,432)



def displayValues(**data):
    print(data)

displayValues(chap1= 10 , chap2 = 20)


def displaydata(info):
    print(info)


displaydata([10,20,30,40])