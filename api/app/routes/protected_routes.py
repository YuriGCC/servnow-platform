# routes/protected_routes.py
from fastapi import APIRouter, Depends
from api.app.routes.deps import get_current_user
from api.app.schemas.user import UserRead
router = APIRouter()

@router.get("/me", response_model=UserRead)
def read_users_me(current_user=Depends(get_current_user)):
    return current_user