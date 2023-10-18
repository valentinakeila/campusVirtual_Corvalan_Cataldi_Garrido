from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo: int, anio_inscripcion_carrera: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__mis_cursos = []

    

    def __str__(self):
        return super().__str__() + " Legajo: ", self.__legajo, " Año de inscripcion: ",self.__anio_inscripcion_carrera

    def matricular_en_curso():
        
        return 

    #decorador classmethod, parametro cls, cuando el profe haga dictar curso esto agregara cursos a su lista mis_cursos,

