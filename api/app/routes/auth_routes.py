from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.app.db.session import get_db
from api.app.models.user import User
from api.app.schemas.user import UserCreate, UserRead, Token
from api.app.utils.security import hash_login, verify_login, create_access_token

router = APIRouter()

@router.post('/register', response_model=UserRead)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_in.email).first()
    if user:
        raise HTTPException(status_code=400, detail='Email já registrado')

    hashed_login = hash_login(user_in.login)
    new_user = User(email=user_in.email, login=hashed_login)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post('/login', response_model=Token)
def login(user_in: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_in.email).first()
    if not user or not verify_login(user_in.login, user.login):
        raise HTTPException(status_code=401, detail='Credenciais Inválidas')
    token = create_access_token(data={'sub': user.email})
    return {'acess_token': token, 'token_type': 'bearer'}
