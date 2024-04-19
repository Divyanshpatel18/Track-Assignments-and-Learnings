# 1.docker build: Build an image from a Dockerfile.
#   CREATES IMAGE WITH DEFAULT IMAGEID
    # docker build .

#  CREATES IMAGE WITH TAGNAME AS my_image
    # docker build -t my_image .

#  TO LIST IMAGES
    # docker image ls

#  TO DELETE IMAGES
    # docker rmi my_image

#2. docker run: Run a container from an image.
 
    # docker run <IMAGEID>(<IMAGENAME>)
    # docker run --name <CONTAINER NAME> <IMAGEID> (adding the name to container)
    # docker run -d <IMAGEID> (running container in detached mode)
    # docker run -p 3000:3000 <IMAGEID>(port binding)
    # docker run --rm <IMAGEID>(automatically removing the container when you stop the container)
    # docker run -it <IMAGEID>(running container in interactive mode i.e. taking input from the user) 
    # docker ps (list of running docker)
    # docker ps -a (list of all containers running and not running)
    # docker stop <CONTAINER NAME>(or default contaier name)(stops the container)
    # docker rm <CONTAINER NAME>( remove the container)

#3. docker logs: Fetch the logs of a container.
#    docker logs my_container

#4. docker pull: Pull an image from a registry.
#    docker pull nginx

#5. docker push: Push an image to a registry.
#    docker push my_image

#6 docker network: Manage Docker networks.
#    docker network ls

    # DOCKER VOLUMES
#    docker volume <VOLUMENAME>
#    docker volume ls
#    docker volume inspect [VOLUME_NAME]
#    docker volume rm [VOLUME_NAME]
#    docker run -v [VOLUME_NAME]:[CONTAINER_PATH] [IMAGE_NAME]
#    ( running a container, you can mount a volume using the -v or --mount option:)
#    docker run -v [HOST_PATH]:[CONTAINER_PATH] [IMAGE_NAME]
#    (Bind Mounts:mount host directories into a container. useful during development/sharing files between the host and container.)


#   MYSQL
#    docker pull mysql
#    docker run  -env MYSQL_ROOT_PASSWORD="root" -env MYSQL_DATABASE="userinfo" --name mysqldb mysql

