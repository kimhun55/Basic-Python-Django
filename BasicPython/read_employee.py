import pymysql.cursors
from Utils import*

connection = Utils.connectdb.getConnection()

try:
    cursor = connection.cursor()

    sql = "SELECT * FROM employee"

    cursor.execute(sql)

    for row in cursor:
        print(row)

except pymysql.Error as e:
    print("Error", e)
finally:
    connection.close()
