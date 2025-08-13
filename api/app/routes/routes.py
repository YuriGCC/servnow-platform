from fastapi import APIRouter
from api.app.routes.service_routes import router as service_router
from api.app.routes.protected_routes import router as protected_routes
from api.app.routes.auth_routes import router as auth_router

router = APIRouter()
all_routes = [router, auth_router, service_router, protected_routes]
@router.get('/')
async def root():
    return {'message': 'hello world'}