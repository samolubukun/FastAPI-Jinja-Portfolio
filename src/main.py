from fastapi import Depends, FastAPI, HTTPException, Body, Request, Form, UploadFile, WebSocket, WebSocketDisconnect, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse, Response
from typing import Annotated
import uvicorn

app = FastAPI()

# Set up templates and static files
templates = Jinja2Templates(directory="../templates")  # Change this path accordingly
app.mount("/static", StaticFiles(directory="../templates/static"), name="static")

# Routes
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# Run the app
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
