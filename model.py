from pydantic import BaseModel 



class Graficos(BaseModel):
    id: int
    titulo: str
    descripcion: str
    imagen: str 