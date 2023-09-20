from fastapi import FastAPI
from api import router as api_router
import uvicorn


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
