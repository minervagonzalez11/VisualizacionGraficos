from pydantic import BaseModel 



class Item(BaseModel):
    descripccion: str 
    status:str

class todo (BaseModel):
    id: int 
    item: str  