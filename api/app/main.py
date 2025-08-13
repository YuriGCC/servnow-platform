from fastapi import FastAPI
from api.app.routes.routes import all_routes

app = FastAPI()

for router in all_routes:
    app.include_router(router)


