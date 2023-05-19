import pymysql
import mysql.connector

def ConnectDB():
    myConection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "game"
    )
    return myConection

def Insert(nickname, score):
    myConection = ConnectDB()
    myCursor = myConection.cursor()

    myCursor.execute(f'INSERT INTO scores(nickname, score) VALUES ("{nickname}", "{score}")')
    
    myConection.commit()
    myConection.close()

def Read():
    myConection = ConnectDB()
    myCursor = myConection.cursor()
    myCursor.execute('SELECT nickname, score FROM scores')

    for nickname, score in myCursor.fetchall():
        print(f"\nNickname: {nickname} score: {score}")

    myConection.close

def Delete(id):
    myConection = ConnectDB()
    myCursor = myConection.cursor()

    myCursor.execute(f'DELETE FROM Estudiantes WHERE id_estudiante = {id}')
    
    myConection.commit()
    myConection.close()