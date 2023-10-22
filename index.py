from usuario import *
from estudiante import *
from profesor import *
from cursos import *

curso1 = Cursos("Programacion I")
curso2 = Cursos("Programacion II")
curso3 = Cursos("Laboratorio I")
curso4 = Cursos("Laboratorio II")
curso5 = Cursos("Ingles I")
curso6 = Cursos("Ingles II")



cursos = [curso1,curso2,curso3,curso4,curso5,curso6]

alumno1 = Estudiante("Nicolas", "Cataldi", "nicolascataldi1@gmail.com", "12354", 2003)
alumno2 = Estudiante("Valentina", "Garrido", "valentinake@gmail.com", "tucontraseñarealaqui", 2009)
alumno3 = Estudiante("Armando", "Codigo", "n", "n", 2023)

alumnos = [alumno1, alumno2, alumno3]

profesor1 = Profesor("Mechi","Valoni","n","n","Analista en Sistemas",2020)
profesor2 = Profesor("Miguel","Angel","n1","n1","Analista en Sistemas",2023)

profesores = [profesor1,profesor2]


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
            menu_estudiante()
            # Opción para ingresar como alumno

        elif respuesta == "2":
            menu_profesor()
            # Opción para ingresar como profesor

        elif respuesta == "3":
            ver_cursos()
            # Opción para ver curso

        elif respuesta == "4":
            # Opción para salir
            print("Hasta Luego!")
            break

        else:
            print("Opcion no valida.")


def menu_estudiante():
    resultado_login = False
    alumno_indice = 0

    print("Ingrese sus credenciales")
    credencial_email = input("Email: ")
    credencial_contrasenia = input("Contraseña: ")

    for i in alumnos:
        alumno_indice = alumno_indice + 1 #Esto es necesario aunque no lo parezca
        if credencial_email == i.email and credencial_contrasenia == i.contrasenia:
            i.nombre
            resultado_login = True
            break

    if resultado_login == True:
        alumno_indice = alumno_indice - 1 #Esto tambien
        opcion_alumno = ""
        contrasenia_curso = ""
        bandera_tiene_cursos = False
        contador_cursos = 0
        bandera_hay_cursos = False

        while opcion_alumno != "3":
            bandera_curso_encontrado = False
            print("1 - Matricularse a un curso")
            print("2 - Ver curso")
            print("3 - Volver al menu principal")
            opcion_alumno = input("\nIngrese una opcion del menu: ")
            if opcion_alumno == "1":
                opcion_curso = input(
                "1 Programación I\n2 Programación II\n3 Laboratorio I\n4 Laboratorio II\n5 Ingles I\n6 Ingles II\n")
                opcion_curso = int(opcion_curso) 
                opcion_curso = opcion_curso - 1

                for i in cursos:
                    if i.alta == True:
                        bandera_hay_cursos = True

                if bandera_hay_cursos == False:
                    print("No hay cursos disponibles")

                if opcion_curso < 6 and opcion_curso > -1:
                    if cursos[opcion_curso].alta == True:
                        for i in range(0,len(alumnos[alumno_indice].mis_cursos)):
                            if cursos[opcion_curso] == alumnos[alumno_indice].mis_cursos[i]:
                                bandera_curso_encontrado = True
                                print("Ya esta matriculado a este curso")
                        if bandera_curso_encontrado == False:
                            contrasenia_curso = input("Ingrese la contraseña del curso\n")
                            if contrasenia_curso == cursos[opcion_curso].contrasenia:
                                print("Matriculado con exito")
                                alumnos[alumno_indice].mis_cursos.append(cursos[opcion_curso].nombre)
                            else:
                                print("Contraseña incorrecta")
                if opcion_curso < 0 or opcion_curso > 5:
                    print("Opcion no valida\n")
                elif cursos[opcion_curso].alta == False:
                    print("El curso no esta disponible\n")
            elif opcion_alumno == "2":
                numero_curso = 0
                for i in alumnos[alumno_indice].mis_cursos:
                    numero_curso = numero_curso + 1
                    bandera_tiene_cursos = True
                    print(numero_curso, "\t", i)

              
                if bandera_tiene_cursos == True:
                    opcion_mostrar_curso = input("Seleccione una opcion\n")
                    opcion_mostrar_curso = int(opcion_mostrar_curso)
                    if opcion_mostrar_curso > len(alumnos[alumno_indice].mis_cursos) or opcion_mostrar_curso < 1:
                        print("Opcion no valida")
                    else:
                        print("Nombre: ", alumnos[alumno_indice].mis_cursos[opcion_mostrar_curso - 1])
                else:
                    print("No esta matriculado a ningun curso")
                print("\n")

            elif opcion_alumno == "3":

                break

            else:
                print("Opcion no valida.")

    else:
        print("Error, debe darse de alta en el alumnado")


def ver_cursos():
    lista_cursos = {
        "Ingles I": "Tecnicatura Universitaria en Programación",
        "Ingles II": "Tecnicatura Universitaria en Programación",
        "Laboratorio I": "Tecnicatura Universitaria en Programación",
        "Laboratorio II": "Tecnicatura Universitaria en Programación",
        "Programación I": "Tecnicatura Universitaria en Programación",
        "Programación II": "Tecnicatura Universitaria en Programación"
    }
    for materia, carrera in lista_cursos.items():
        print(f"Materia: {materia}\t\t\tCarrera: {carrera}")
    print("\n")

def menu_profesor():
    resultado_login = False
    profesor_indice = 0

    print("Ingrese sus credenciales")
    credencial_email = input("Email: ")
    credencial_contrasenia = input("Contraseña: ")

    for i in profesores:
        profesor_indice = profesor_indice + 1
        if credencial_email == i.email and credencial_contrasenia == i.contrasenia:
            i.nombre
            resultado_login = True
            break

    if resultado_login == True:
        profesor_indice = profesor_indice - 1
        opcion_profesor = ""
        contrasenia_curso = ""
        bandera_tiene_cursos = False
        contador_cursos = 0
        bandera_hay_cursos = False

        while opcion_profesor != "3":
            bandera_curso_encontrado = False
            print("1 - Dictar curso")
            print("2 - Ver curso")
            print("3 - Volver al menu principal")
            opcion_profesor = input("\nIngrese una opcion del menu: ")
            if opcion_profesor == "1":
                opcion_curso = input(
                "1 Programación I\n2 Programación II\n3 Laboratorio I\n4 Laboratorio II\n5 Ingles I\n6 Ingles II\n")
                opcion_curso = int(opcion_curso) 
                opcion_curso = opcion_curso - 1

                for i in cursos:
                    if i.alta == False:
                        bandera_hay_cursos = True

                if bandera_hay_cursos == False:
                    print("No hay cursos disponibles")
                if opcion_curso < 6 and opcion_curso > -1:
                    if cursos[opcion_curso].alta == True:
                        bandera_curso_encontrado = True
                        print("Ya se esta dictando este curso")
                    if bandera_curso_encontrado == False:
                        print("Ahora eres el profesor de este curso")
                        cursos[opcion_curso].alta = True
                        profesores[profesor_indice].mis_cursos.append(cursos[opcion_curso].nombre)
                        print(f"Curso a dictar: {cursos[opcion_curso].nombre}\nContraseña: {cursos[opcion_curso].contrasenia}\n")
                else:
                    print("El curso no esta disponible\n")
                    
            elif opcion_profesor == "2":
                numero_curso = 0
                for i in profesores[profesor_indice].mis_cursos:
                    numero_curso = numero_curso + 1
                    bandera_tiene_cursos = True
                    print(numero_curso, "\t", i)

              
                if bandera_tiene_cursos == True:
                    opcion_mostrar_curso = input("Seleccione una opcion\n")
                    opcion_mostrar_curso = int(opcion_mostrar_curso)
                    if opcion_mostrar_curso > len(profesores[profesor_indice].mis_cursos) or opcion_mostrar_curso < 1:
                        print("Opcion no valida")
                    else:
                        print("Nombre: ", profesores[profesor_indice].mis_cursos[opcion_mostrar_curso - 1])
                else:
                    print("No esta dictando ningun curso")
                print("\n")
            elif opcion_profesor == "3":

                break

            else:
                print("Opcion no valida.")


menu()
