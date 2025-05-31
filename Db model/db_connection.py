import pymysql

#DB connection 

def get_connection():

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='juanes09',
        database='exito_smartphones_db',
        port=3306
    )
    return connection
     

    



