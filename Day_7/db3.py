#step1
import pymysql
import csv

try:
    db = pymysql.connect(host='localhost',port=3306,user='root',password='india@123',database='jntuk')
    print(db)
    # create your query/handler/reference
    cursor = db.cursor()
    # prepare your query
    # file handling
    with open("realestate.csv","r") as fobj:
        #convert file object to csv object
        reader = csv.reader(fobj)
        for record in reader:
            query =  "insert into realestate values('{}','{}')".format(record[0],record[1])
            cursor.execute(query)   
    #make the changes permanent
            db.commit()

    db.close()
except pymysql.DatabaseError as err:
    print("Database error .. Exception raised for errors that are related to the database.")
    print(err)

except pymysql.OperationalError as err:
    print("related to the database'soperation")
    print(err)
    
except pymysql.IntegrityError as err:
    print("Related to keys")
    print(err)
except Exception as err:
    print(err)
    