from usuario import *
from estudiante import *
from profesor import *
from cursos import *

alumno1 = Estudiante("Nicolas","Cataldi","nicolascataldi1@gmail.com","9014")
alumno2 = Estudiante("Valen","Garrido","nosetumailperoacaestaria@quiensabe.algo","tucontraseñarealaqui")
alumnos = [alumno1,alumno2]

def menu():
    respuesta = ""
    print("Bienvenido!")
    while respuesta != "4":
        print("1 - Ingresar como alumno")
        print("2 - Ingresar como profesor")
        print("3 - Ver curso")
        print("4 - Salir")
        respuesta = input("\nIngrese una opcion del menu: ")
        if respuesta == "1":
            menu_usuario()
            # Opción para ingresar como alumno

        elif respuesta == "2":
            ""
            # Opción para ingresar como profesor

        elif respuesta == "3":
            ""
            # Opción para ver curso

        elif respuesta == "4":
            # Opción para salir
            print("Hasta Luego!")
            break

        else:
            print("Opcion no valida.")
def menu_usuario():
    resultado_login = False

    print("Ingrese sus credenciales")
    credencial_email = input("Email: ")
    credencial_contrasenia = input("Contraseña: ")

    for i in alumnos:
        if credencial_email == i.email and credencial_contrasenia == i.contrasenia:
            resultado_login = True
            break

    if resultado_login == True:
        opcion_alumno = ""
        while opcion_alumno != "3":
            print("1 - Matricularse a un curso")
            print("2 - Ver curso")
            print("3 - Volver al menu principal")
            opcion_alumno = input("\nIngrese una opcion del menu: ")

    else:
        print("Error, debe darse de alta en el alumnado")

menu()


