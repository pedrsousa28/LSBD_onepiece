import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='onepiece',
)

cursor = cnx.cursor()

cmd = f'SELECT * FROM personagens'
cursor.execute(cmd)
cnx.commit()
result = cursor.fetchall()


cursor.close()
cnx.close()