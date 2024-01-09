from fastapi import FastAPI
from extra_task.webController import router

def run():
    app = FastAPI()
    app.include_router(router)

