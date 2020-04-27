import pymysql.cursors
from Utils import *


connection = Utils.connectdb.getConnection()

try:
    cursor = connection.cursor()

    sql = "INSERT INTO employee (emp_no,emp_name,emp_salary) VALUES(%s,%s,%s)"

    cursor.execute(sql, ('1', 'kimhun55', '20000'))
    connection.commit()
    print("create New insert")
except pymysql.Error as e:
    print("Error", e)
finally:
    connection.close()
