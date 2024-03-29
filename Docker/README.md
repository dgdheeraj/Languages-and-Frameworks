# Docker

## What is Virtualization?


## What is Docker?
Tool that allows developers to deploy applications in a sandbox (container) to run on the host OS. Key advantage of Docker is to package application with all of its dependencies into a standardized unit. Unlike virtual machines, containers do not have high overhead and hence enable more efficient usage of the underlying system and resources

## Containers?
Virtual Machines have high overhead spent virtualizing hardware for a guest OS to use.
Containers leverage the mechanics of the host OS to provide the kind of isolation VMs provide at a lower computing power.

Containers are portable since it can be deployed in any environment that supports containerization.

## Defniitions
- <b>Images</b>: Blueprint of the application which is the basis of a container. 
- <b>Container</b>: Created from images and run the actual application.
- <b>Docker Daemon</b>: The background service running on the host that manages building, running and distributing Docker containers.


## Tutorial

```
# Pull image from registry
docker pull busybox

# Lists all the images
docker images

# Run a particular image
docker run busybox

# Shows currently running containers
docker ps

# Shows all containers
docker ps -a
```

Docker Run with it flag
`docker run -it busybox sh`, attaches an interactive tty to the container. THis is basically a terminal


Delete containers which are not running
```
docker rm $(docker ps -a -q -f status=exited)
```
-a : returns all containers
-q : returns only numeric IDs
-f : filters output based on condition (this case status)

`docker container prune` gives the same result as above

`docker rmi <image_name>` to delete any image from system

```
docker run --rm -it prakhar1989/static-site
```
--rm : automaitcally removes container when it exits
-it  : attaches interactive terminal 



```
docker run -d -P --name static-site prakhar1989/static-site
```
-d   : runs the container in detached mode ()
--rm : automatically removes container when it exits
-it  : attaches interactive terminal 
-P   : publish all exposed ports to random ports
--name:gives a name to the running container

```
docker run -p 8888:80 prakhar1989/static-site
```
Specify a custom port to which the port 80 in the container will map to

## Images

- Base images: Images that have no parent image, usually images with an OS like ubuntu, busybox or debian.
- Child images: Images that build on base images and add additional functionality.

# Dockerfile
A text file that contains list of commands that docker client will run while creating an image

Example file

```
# Specify base image
FROM python:3.8

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./app.py"]
```

Building image from Dockerfile
```
docker build -t dgdheeraj/catnip .
```
. -> location of directory containing the Dockerfile
-t : name for the image

## Multi - Container Environments

### Docker Network
When docker is installed, it creates three networks automatically.
- bridge: Network in which containers are run by default 
- host
- none

```
# To inspect a particular network
docker network inspect bridge
```


```
# Creates a new bridge network 
docker network create foodtrucks-net
```


```
docker run --net <N/W name>
```
Launches the container in that particular N/W


You can also resolve a container name to an IP address. This capability is called automatic service discovery

## Docker Compose

- Compose is a tool that is used for defining and running multi-container Docker apps in an easy way
- It provides a configuration file called docker-compose.yml that can be used to bring up an application and the suite of services it depends on with just one command

Docker Compose creates a new network for all the containers included in the file

```
version: "3"
services:
  es:
    image: docker.elastic.co/elasticsearch/elasticsearch:6.3.2
    container_name: es
    environment:
      - discovery.type=single-node
    ports:
      - 9200:9200
    volumes:
      - esdata1:/usr/share/elasticsearch/data
  web:
    image: yourusername/foodtrucks-web
    command: python3 app.py
    depends_on:
      - es
    ports:
      - 5000:5000
    volumes:
      - ./flask-app:/opt/flask-app
volumes:
  esdata1:
    driver: local
```

```
docker compose up -d
```
Start all the containers


```
docker-compose down -v
```
Destroy the cluster and data volumes 

# Links

- [Docker Curriculum](https://docker-curriculum.com/)

Note: See the above link for AWS Stuff