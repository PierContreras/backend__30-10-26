from fastapi import APIRouter, HTTPException

from ..schemas.estudiante import Estudiante, EstudianteActualizar
from ..services.estudiante_service import EstudianteService

rutaEstudiante = APIRouter(prefix="/estudiante", tags=["Estudiante"])

estudianteServicio = EstudianteService()


@rutaEstudiante.post("/")
def guardarEstudiante(estudianteNuevo: Estudiante):
    try:
        return estudianteServicio.guardarEstudiante(estudianteNuevo)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@rutaEstudiante.get("/")
def mostrarEstudiante():
    return estudianteServicio.mostrarEstudiante()


@rutaEstudiante.put("/{id}")
def actualizarEstudiante(id: int, estudianteActualizar: EstudianteActualizar):
    try:
        return estudianteServicio.actualizarEstudiante(id, estudianteActualizar)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@rutaEstudiante.delete("/{id}")
def eliminarEstudiante(id: int):
    try:
        return estudianteServicio.eliminarEstudiante(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
