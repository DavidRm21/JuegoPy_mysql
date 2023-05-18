import pymysql
import mysql.connector

def ConnectDB():
    myConection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database = "Colegio"
    )
    return myConection

def Read():
    myConection = ConnectDB()
    myCursor = myConection.cursor()
    myCursor.execute('SELECT nombre, apellido, notaUno, notaDos, notaTres, notaFinal FROM Estudiantes')

    for nombre, apellido, notaUno, notaDos, notaTres, notaFinal in myCursor.fetchall():
        print("\nNombre: ",nombre, " ", apellido, "\nNota 1: ", notaUno, "\nNota 2: ", notaDos, "\nNota 3: ", notaTres, "\nNota final: ", notaFinal)

    myConection.close

def Insert(name, lastName):
    myConection = ConnectDB()
    myCursor = myConection.cursor()

    myCursor.execute(f'INSERT INTO Estudiantes(nombre, apellido) VALUES ("{name}", "{lastName}")')
    
    myConection.commit()
    myConection.close()

def Insert(name, lastName, notaUno, notaDos, notaTres):
    myConnection = ConnectDB()
    myCursor = myConnection.cursor()
    notaFinal = float(notaUno + notaDos + notaTres) / 3

    myCursor.execute(f'INSERT INTO Estudiantes(nombre, apellido, notaUno, notaDos, notaTres, notaFinal) VALUES ("{name}", "{lastName}", {notaUno}, {notaDos}, {notaTres}, {notaFinal})')

    myConnection.commit()
    myConnection.close()

def Delete(id):
    myConection = ConnectDB()
    myCursor = myConection.cursor()

    myCursor.execute(f'DELETE FROM Estudiantes WHERE id_estudiante = {id}')
    
    myConection.commit()
    myConection.close()

# ------------------------------------------------------------  

continueProgram = True 
options = ["Leer registros de la base de datos", "Insertar solamente nombres y apellidos en la base de datos", "Insertar registro completo en la base de datos","Eliminar registro de la base de datos"]  

while(continueProgram):

    print("\nComandos SQL \n")
    i = 0
    for opc in options:
        i += 1
        print(i, ". ", opc)

    selectedOption = int(input("\nQué sentencia desea aplicar: "))

    match selectedOption:
        case 1:
            Read()
        case 2:
            name = input("Digite el nombre del estudiante: ")
            lastName = input("Digite el apellido del estudiante: ")
            Insert(name, lastName)
        case 3:
            name = input("Digite el nombre del estudiante: ")
            lastName = input("Digite el apellido del estudiante: ")
            notaUno = float(input("Digite la primera nota: "))
            notaDos = float(input("Digite la Segunda nota: "))
            notaTres = float(input("Digite la Tercera nota: "))
            Insert(name, lastName, notaUno, notaDos, notaTres)

        case 4:
            id_e = int(input("Digite el id del registro que desea borrar: "))
            Delete(id_e)
        case _:
            pass        
        
        
    inputContinue = int(input("¿Desea realizar otra sentencia? \n1. Si\n2. No\n\n"))
    if (inputContinue == 2):
        continueProgram = False