from fastapi import FastAPI
from projects.project import router

app = FastAPI()

app.include_router(router.router)
