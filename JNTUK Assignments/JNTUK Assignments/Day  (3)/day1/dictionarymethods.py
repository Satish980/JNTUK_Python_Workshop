


book  = {"chap1":10 ,"chap2":20 ,"chap3":30 ,"chap1":1000}

# ONLY KEYS
print(book.keys())

## ONLY VALUES
print(book.values())

print(book.items())

#print(book["chap10"])

print(book.get("chap100"))

# chap1-10 will be removed
book.pop("chap1")
print(book)

book2 = {"chap6":60}

book.update(book2)
print(book)



