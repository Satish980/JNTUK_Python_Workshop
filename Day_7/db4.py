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
    fobj = open("realestate_18082020.csv","w")
    for record in cursor.fetchall():
        #print(record)
        fobj.write(",".join(record) + "\n")
    # close the connection
    fobj.close()
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
    