from pydantic import BaseModel

class ServiceCreate(BaseModel):
    name: str
    price: int

class ServiceRead(BaseModel):
    id: int
    name: str
    price: int

    class Config:
        orm_nome = True