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

print(curso1.contrasenia)
print(curso2.contrasenia)
print(curso3.contrasenia)
print(curso4.contrasenia)
print(curso5.contrasenia)
print(curso6.contrasenia)




alumno1 = Estudiante("Nicolas", "Cataldi", "nicolascataldi1@gmail.com", "12354", 2003)
alumno2 = Estudiante("Valen", "Garrido", "nosetumailperoacaestaria@quiensabe.algo", "tucontraseñarealaqui", 2009)
alumno3 = Estudiante("Armando", "Codigo", "n", "n", 2023)

alumnos = [alumno1, alumno2, alumno3]


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
            ""
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
        alumno_indice = alumno_indice + 1
        if credencial_email == i.email and credencial_contrasenia == i.contrasenia:
            i.nombre
            resultado_login = True
            break

    if resultado_login == True:
        alumno_indice = alumno_indice - 1
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
                        

                if bandera_hay_cursos == False:
                    print("No hay cursos disponibles")

                if opcion_curso == "1":
                    if curso1.alta == True:
                        for i in alumnos[alumno_indice].mis_cursos:
                            if i == "Programacion I":
                                bandera_curso_encontrado = True
                                print("Ya esta matriculado a este curso")
                        if bandera_curso_encontrado == False:
                            contrasenia_curso = input("Ingrese la contraseña del curso\n")
                            if contrasenia_curso == curso1.contrasenia:
                                print("Matriculado con exito")
                                alumnos[alumno_indice].mis_cursos.append("Programacion I")
                            else:
                                print("Contraseña incorrecta")
                    else:print("El curso no esta disponible")

                elif opcion_curso == "2":
                    for i in alumnos[alumno_indice].mis_cursos:
                        if i == "Programacion II":
                            bandera_curso_encontrado = True
                            print("Ya esta matriculado a este curso")
                    if bandera_curso_encontrado == False:
                        contrasenia_curso = input("Ingrese la contraseña del curso\n")
                        if contrasenia_curso == curso2.contrasenia:
                            print("Matriculado con exito")
                            alumnos[alumno_indice].mis_cursos.append("Programacion II")
                        else:
                            print("Contraseña incorrecta")
                elif opcion_curso == "3":
                    for i in alumnos[alumno_indice].mis_cursos:
                        if i == "Laboratorio I":
                            bandera_curso_encontrado = True
                            print("Ya esta matriculado a este curso")
                    if bandera_curso_encontrado == False:
                        contrasenia_curso = input("Ingrese la contraseña del curso\n")
                        if contrasenia_curso == curso3.contrasenia:
                            print("Matriculado con exito")
                            alumnos[alumno_indice].mis_cursos.append("Laboratorio I")
                        else:
                            print("Contraseña incorrecta")
                elif opcion_curso == "4":
                    for i in alumnos[alumno_indice].mis_cursos:
                        if i == "Laboratorio II":
                            bandera_curso_encontrado = True
                            print("Ya esta matriculado a este curso")
                    if bandera_curso_encontrado == False:
                        contrasenia_curso = input("Ingrese la contraseña del curso\n")
                        if contrasenia_curso == curso4.contrasenia:
                            print("Matriculado con exito")
                            alumnos[alumno_indice].mis_cursos.append("Laboratorio II")
                        else:
                            print("Contraseña incorrecta")
                elif opcion_curso == "5":
                    for i in alumnos[alumno_indice].mis_cursos:
                        if i == "Ingles I":
                            bandera_curso_encontrado = True
                            print("Ya esta matriculado a este curso")
                    if bandera_curso_encontrado == False:
                        contrasenia_curso = input("Ingrese la contraseña del curso\n")
                        if contrasenia_curso == curso5.contrasenia:
                            print("Matriculado con exito")
                            alumnos[alumno_indice].mis_cursos.append("Ingles I")
                        else:
                            print("Contraseña incorrecta")
                elif opcion_curso == "6":
                    for i in alumnos[alumno_indice].mis_cursos:
                        if i == "Ingles II":
                            bandera_curso_encontrado = True
                            print("Ya esta matriculado a este curso")
                    if bandera_curso_encontrado == False:
                        contrasenia_curso = input("Ingrese la contraseña del curso\n")
                        if contrasenia_curso == curso6.contrasenia:
                            print("Matriculado con exito")
                            alumnos[alumno_indice].mis_cursos.append("Ingles II")
                        else:
                            print("Contraseña incorrecta")

            elif opcion_alumno == "2":
                numero_curso = 0
                for i in alumnos[alumno_indice].mis_cursos:
                    numero_curso = numero_curso + 1
                    bandera_tiene_cursos = True
                    print(numero_curso, "\t", i)

                opcion_mostrar_curso = input("Seleccione una opcion\n")
                opcion_mostrar_curso = int(opcion_mostrar_curso)
                print("Nombre: ", alumnos[alumno_indice].mis_cursos[opcion_mostrar_curso - 1])

                if bandera_tiene_cursos == False:
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


menu()
