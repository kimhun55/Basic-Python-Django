import pymysql.cursors

# function connect db and return connection


def getConnection():
    connection = pymysql.Connection(
        host='localhost',
        user='root',
        password='',
        db='pythontestdb',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


# print(getConnection())
