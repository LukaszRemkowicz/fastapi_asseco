FROM python:3.10-alpine as development

EXPOSE 8080

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
RUN ln -sf /usr/share/zoneinfo/Europe/Warsaw /etc/timezone && \
    ln -sf /usr/share/zoneinfo/Europe/Warsaw /etc/localtime
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

RUN mkdir /fastapi_app
WORKDIR /fastapi_app

RUN mkdir /server

COPY . /fastapi_app/server


RUN adduser -u 5678 --disabled-password --gecos "" user && chown -R user /fastapi_app
USER user

CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]

FROM development as production
RUN mkdir -p /fastapi_app/server/_logs
