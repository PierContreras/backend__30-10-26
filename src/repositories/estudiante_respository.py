from ..schemas.estudiante import Estudiante, EstudianteActualizar

class EstudianteRepository:

    def __init__(self):
        self.__listaEstudiantes = list[Estudiante] = [] 

    def guardar_estudiante(self, estudianteNuevo: Estudiante):
        self.__listaEstudiantes.append(estudianteNuevo)
        return estudianteNuevo

    def mostrar_estudiantes(self):
        return self.__listaEstudiantes

    def actualizar_estudiante(self, id, estudianteActualizar: EstudianteActualizar):
        try:
            for _, valor in enumerate(self.__listaEstudiantes):
                if valor.id == id:
                    valor.nombre = estudianteActualizar.nombre
                    valor.edad = estudianteActualizar.edad
                    valor.correo = estudianteActualizar.correo
                    return valor
            return None
        except Exception as e:
            raise str(e)

    def eliminar_estudiante(self, id):
        try:
            for i, valor in enumerate(self.__listaEstudiantes):
                if valor.id == id:
                    self.__listaEstudiantes.pop(i)
                    return id
            return None
        except Exception as e:
            raise str(e)