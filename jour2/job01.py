# import sqlite3
# conn=sqlite3.connect(':memory:')
# cursor=conn.cursor()
# cursor.execute("""SELECT nom , prenom, age, email FROM etudiant""")
# rows = cursor.fetchall()
# for row in rows:
#     print('{0}:{1}-{2}'.format(row[0],row[1],row[2]))

import mysql.connector
cnx=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database = "LaPlateforme")

mycursor = cnx.cursor()
mycursor.execute("SELECT * from etudiant")

for i in mycursor:
    print(i)
if cnx.is_connected():
    print("connexion reussit a mysql")

#job4
mycursor.execute("select nom, capacite from salle;")
for i in mycursor:
    print(i)


cnx.close()
