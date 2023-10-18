from usuario import *
from estudiante import *
from profesor import *
from cursos import *

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Ingresar como alumno")
    print("2 - Ingresar como profesor")
    print("3 - Ver curso")
    print("4 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese una opción de menú: ")
    if opt.isnumeric():
        if int(opt) == 1:
            
           
        elif int(opt) == 2:
           
           
        elif int(opt) == 3:
         
        elif int(opt) == 4:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")

print("Hasta luego!.")