import mysql.connector
from mysql.connector import Error
def insertdata():
    try:
        connection=mysql.connector.connect(host='localhost',
                                           database='products',
                                           user='root',
                                           password='18910352@#aA'
                                           )
        if(connection.is_connected()):
            db_info=connection.get_server_info()
            print("Connection to MySQL version ",db_info)
            cursor=connection.cursor()
            cursor.execute('select database();')
            record=cursor.fetchone()
            print("You are connected to ",record)####data table taken from online source
        createtable="""CREATE TABLE IF NOT EXISTS products (
             productID    INT UNSIGNED  NOT NULL AUTO_INCREMENT,
             productCode  CHAR(3)       NOT NULL DEFAULT '',
             name         VARCHAR(30)   NOT NULL DEFAULT '',
             quantity     INT UNSIGNED  NOT NULL DEFAULT 0,
             price        DECIMAL(7,2)  NOT NULL DEFAULT 99999.99,
             PRIMARY KEY  (productID)
             );"""
        cursor = connection.cursor()
        result = cursor.execute(createtable)
        print("products Table created successfully ")

        insert_data='''insert into products values(%s,%s,%s,%s,%s)'''
        records=[(1001, 'PEN', 'Pen Red', 5000, 1.23),
                (1002, 'PEN', 'Pen Blue',  8000, 1.25),
                (1003, 'PEN', 'Pen Black', 2000, 1.25),
                (1004,'PEC', 'Pencil 2B', 10000, 0.48),
                (1005,'PEC', 'Pencil 2H', 8000, 0.49)
                 ]
        cursor=connection.cursor()
        cursor.executemany(insert_data,records)
        connection.commit()
        print(cursor.rowcount," record succesfully inserted")
        
        
    except Error as e:
        print("Error while connecting to database ",e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
print(insertdata())
def fetch():
    try:
        connection=mysql.connector.connect(host='localhost',
                                               database='products',
                                               user='root',
                                               password='18910352@#aA'
                                               )
        cursor=connection.cursor()
        cursor.execute("select * from products")
        for row in cursor.fetchall():
            print('\n')
            yield row
            
    except Error as e:
        print("Error while connecting to database ",e)
print(list(fetch()))

