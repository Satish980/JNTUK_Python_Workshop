#!/usr/bin/python

# Dictionaries in python
dict = {'Subject':'Physics','Year':2014,'Marks':88}

# to print complete dictionary
print("Complete dict : ", dict )

# If we attempt to access a data item a key
# which is not part of the dictionary, we get an error
# to print the values in the dictionary
print("dict['Subject']:",dict['Subject'])
print("dict['Marks']:",dict['Marks'])

# update existing entry
dict['Year'] = 2013

# created a new key with value
dict['School'] = 'Milton High'
print("after new key : ", dict )

# remove individual dictionary elements or clear the entire contents of a dictionary
# remove entry ith key 'Subject'

del dict['Subject']
print("after removing key \'Subject\' : ", dict )

# remove all entries in dict
dict.clear()
print("After removing all entries : ", dict )

# delete entire dictionary
del dict ;
print("dictionary dict deleted.")


# assign dictionaries
dict = {'Subject':'physics','Year':2014,'Marks':88}
adict = {'School':'Milton High'}

# a shallow copy of dictionary dict
dict.copy()

# a list of dict's ( key, value ) tuple pairs
dict.items()
print("dict\'s (key,value) tuple pairs :", dict.items())

# list of dictionary dict's keys
dict.keys()
print("dict\'s keys : ",dict.keys())

# list of dictionary dict's values
dict.values()
print("dict\'s values : ", dict.values())

# to add dictionary dict2's key-values pairs to dict
print("Second dictionary adict: ", adict )
dict.update(adict)
print("dict after updation: ", dict )

