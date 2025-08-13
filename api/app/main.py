from fastapi import FastAPI
from api.app.routes.routes import all_routes
import uvicorn

app = FastAPI()

for router in all_routes:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000,reload=True)
