from ..schemas.estudiante import Estudiante, EstudianteActualizar


class EstudianteRepositorio:
    def __init__(self):
        self.__listaEstudiantes = []

    def guardarEstudiante(self, estudianteNuevo: Estudiante):
        self.__listaEstudiantes.append(estudianteNuevo)
        return estudianteNuevo

    def mostrarEstudiantes(self):
        return self.__listaEstudiantes

    def actualizarEstudiante(self, id: int, estudianteActualizar: EstudianteActualizar):
        for estudiante in self.__listaEstudiantes:
            if estudiante.id == id:
                estudiante.nombre = estudianteActualizar.nombre
                estudiante.edad = estudianteActualizar.edad
                estudiante.correo = estudianteActualizar.correo
                return estudiante
        return None

    def eliminarEstudiante(self, id: int):
        for indice, estudiante in enumerate(self.__listaEstudiantes):
            if estudiante.id == id:
                self.__listaEstudiantes.pop(indice)
                return id
        return None

    def guardar_estudiante(self, estudianteNuevo: Estudiante):
        return self.guardarEstudiante(estudianteNuevo)

    def mostrar_estudiantes(self):
        return self.mostrarEstudiantes()

    def actualizar_estudiante(self, id: int, estudianteActualizar: EstudianteActualizar):
        return self.actualizarEstudiante(id, estudianteActualizar)

    def eliminar_estudiante(self, id: int):
        return self.eliminarEstudiante(id)


EstudianteRepository = EstudianteRepositorio
