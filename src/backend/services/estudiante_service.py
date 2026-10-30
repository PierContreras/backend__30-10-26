from ..schemas.estudiante import Estudiante
from ..repositories.estudiante_repository import EstudianteRepositorio


class EstudianteService:
    def __init__(self):
        self.__estudianteRepositorio = EstudianteRepositorio()

    def guardarEstudiante(self, estudianteNuevo: Estudiante):
        try:
            return self.__estudianteRepositorio.guardar_estudiante(estudianteNuevo)
        except Exception as e:
            raise str(e)

    def mostrarEstudiante(self):
        return self.__estudianteRepositorio.mostrarEstudiantes()

    def actualizarEstudiante(self, id: int, estudianteActualizar: Estudiante):
        try:
            return self.__estudianteRepositorio.actualizar_estudiante(id, estudianteActualizar)
        except Exception as e:
            raise str(e)

    def eliminarEstudiante(self, id: int):
        try:
            return self.__estudianteRepositorio.eliminarEstudiante(id)
        except Exception as e:
            raise str(e)