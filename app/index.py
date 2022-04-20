import datetime
import socket
import os

from fastapi.responses import JSONResponse
from fastapi import FastAPI, status, Request
import logging
import logging.config
from app.logging_setup import LOGGING

LOGGING_CONFIG = None
logging.config.dictConfig(LOGGING)
logger = logging.getLogger(f"project.{__name__}")

app=FastAPI()


@app.get('/', status_code=status.HTTP_201_CREATED)
def index(request: Request):


    date_now = datetime.datetime.now()
    date_now = date_now.strftime("%Y.%m.%d, %H:%M")

    # ip_add = ''

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 8000))
    ip_add = s.getsockname()
    s.close()

    server_ip = os.environ.get('SERVER_IP')

    context = {
        'date': date_now,
        'docker_ip_add': ip_add[0],
        'server_ip': server_ip
    }

    return JSONResponse(context)