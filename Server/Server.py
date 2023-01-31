import uvicorn
from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/")
def read_index():
    return FileResponse("Server/index.html")

@app.get("/style.css")
def read_style():
    return FileResponse("style.css")
