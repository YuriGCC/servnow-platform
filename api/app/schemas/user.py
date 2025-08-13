from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    login: str

class UserRead(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    acess_token: str
    token_type: str