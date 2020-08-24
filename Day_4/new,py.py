#Example program3
# combination of an else statement with a for statement that searches for
# prime numbers from 10 thru 20

# to iterate between 10 to 20
print("Example program 3 - FOR ELSE construct \n")
for num in range(10,20):

    # to iterate on the factors of the number
    for increment in range(2,num):
        # to determine the first factor
        if num%increment == 0:
            # to calculate the second factor
            factor = num/increment
            print("%d equals %d * %d " %(num,increment,factor))
            # to move to the next number, the #first FOR
            break          
    else:
        print(num, 'is a prime number')
