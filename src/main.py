from fastapi import Depends, FastAPI, HTTPException, Body, Request, Form, UploadFile, WebSocket, WebSocketDisconnect, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse, Response
from typing import Annotated
import uvicorn
from pathlib import Path

app = FastAPI()

# Get absolute path to the project root folder (2 levels up from main.py)
BASE_DIR = Path(__file__).parent.parent.resolve()

templates_dir = BASE_DIR / "templates"
static_dir = templates_dir / "static"

# Use absolute paths for templates and static
templates = Jinja2Templates(directory=str(templates_dir))
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
app.mount("/assets", StaticFiles(directory=str(templates_dir / "assets")), name="assets")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)