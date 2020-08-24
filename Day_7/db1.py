#step1
import pymysql

try:
    db = pymysql.connect(host='localhost',port=3306,user='root',password='india@123',database='jntuk')
    print(db)
    # create your query/handler/reference
    cursor = db.cursor()
    # prepare your query
    query ="select * from realestate"
    # execute the query
    cursor.execute(query)
    # display the output
    for record in cursor.fetchall():
        print(record)
    # close the connection
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
    