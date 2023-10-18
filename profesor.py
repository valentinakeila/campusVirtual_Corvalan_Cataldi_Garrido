from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio_egreso: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__mis_cursos = []

    def __str__(self):
        return super().__str__() + " Titulo: ", self.__titulo, " Año de egreso: ",self.__anio_egreso

    def dictar_curso():
        
        return 

