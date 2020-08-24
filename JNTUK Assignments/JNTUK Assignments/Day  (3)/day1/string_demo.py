#!/usr/bin/python

# strings in python

str = 'hello world!'
strnew = "python programming"

# If you see a output message complete string
print("complete string:", str )

# You will get the first character of the string
print("first character of the string:", str[0])

# When required hte string starting from 2nd to 5th
print("the string starting from 2nd to 5th:",strnew[1:5])

# To access substrins, use the square brackets
# for slicing along with the index or indicces to obtain your substring

# You can update an existing string by assigning a variable to another string
strupdate = str[:6] + 'Python'
print("Updated string :-", strupdate )

#to assign substring to be searched
sub = "P"

# The substring is searched between 0 to 10
print("Subsring is searched:",strnew.count(sub))
print("Substring is searched between 0 to 10 :",strnew.count(sub,0,10))

# to specify the string to be searched
sub = "Prog"

# to print the index if found and -1 otherwise
print("Search a substring \'Prog\' in the string : ", strnew.find(sub,50))

# assign seperator string and get output as concatenation of the strings in the seq

str = "-"
seq = ("Easy","to","Use")
print("Join string with a separated character :", str.join(seq))

#to get the length of the string
print("Length of the string: ", len(strnew))

strnew = "0000000000Python Programming00000000"

#to print a copy of the string in which all chars have been stripped from the
# beginning and the end of the string
print("Strip the leading and trailing zeros in a string:", strnew.strip('0'))

strnew = "Python Programming"
# to list of all the words in the string, using strnew as the separator
#( splits on all whitespace if left unspecified )
#optionally limiting the number of splits to num
print("Split a string: ", strnew.split())

# to replace a copy of the string with all occurrences of substring old replaced by num
print(strnew.replace("Python","Perl"))
