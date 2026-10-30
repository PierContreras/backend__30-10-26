from fastapi import FastAPI
from .apis.estudiante_api import rutaEstudiante

app = FastAPI(title="Backend")

app.include_router(rutaEstudiante, prefix="/api")


def main():
    import uvicorn

    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000)