from datetime import datetime
import socket
import os

from fastapi.responses import JSONResponse
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from server.app.logging_setup import logger

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

app=FastAPI()


origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://127.0.0.1:3000",
    "127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', status_code=status.HTTP_200_OK)
def index() -> JSONResponse:

    date_now = datetime.now()
    date_now = date_now.strftime("%Y.%m.%d, %H:%M")

    socket_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_ip.connect(("8.8.8.8", 8000))
    ip_add = socket_ip.getsockname()
    socket_ip.close()

    server_ip = os.getenv('SERVER_IP')

    context = {
        'date': date_now,
        'docker_ip_add': ip_add[0],
        'server_ip': server_ip
    }

    return JSONResponse(context)
