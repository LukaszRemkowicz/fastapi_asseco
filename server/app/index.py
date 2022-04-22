import datetime
from pprint import pprint
import socket
import os

from fastapi.responses import JSONResponse
from fastapi import FastAPI, status, Request
from server.app.logging_setup import logger

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

app=FastAPI()


@app.get('/', status_code=status.HTTP_201_CREATED)
def index():

    date_now = datetime.datetime.now()
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
