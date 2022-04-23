
## Microservice based on FastApi and React

### App includes only one endpoint which returns dictionary object with ip and current date

<br>
<br>

# Instructions:

* Copy repo on your local disc
* To have your server ip showed on the website add .env file to main folder of aplication.
* Add variable to file: SERVER_IP=your host ip address
* To run server, use command from working directiory: 
```bash
uvicorn server.app.index:app  --host 0.0.0.0 --reload --port 8080
```
* To run Reactapp, go to client server and in terminal write: 
```bash
npm start
```

# Dockerize it!
* To use docker, go to main directory (which contains docker-compose file) and write in terminal:
```bash
docker-compose up --build
```

Windows users:

>to share your host volumes with ReactApp, you have to disable WSL2 in your Desktop Docker (settings -> general). To disable it, you have to first enable Hyper-V: [link](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v).

<br>
<br>

## INFO:
Application contains full workflow (github actions):
* After pushing to your repo and doing pull request, github actions creates docker images and tests it.
* if pushing to production branch, github action pushing images to docker hub. To use it, add secret keys to your repositorium with: DOCKER_PASSWORD, DOCKER_USER
* docker-compose.prod.yml contains copy of dev docker-compose file except using volumes.

## How it looks like:
![alt text](reactapp.jpg?raw=true)