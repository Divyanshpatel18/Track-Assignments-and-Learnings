
 # INSTRUCTIONS arguement
#  base image refers to the starting point for creating a new Docker container. 
# It's essentially the foundation upon which your container image is built.
# FROM to specify the base image which can be pulled from container registry(dockerHub)
FROM node:16

# Set the working directory in the container(docker run myimage pwd :check in which folder image is running)
# will create a folder myapp and change the directory to myapp after build
WORKDIR /myapp

# RUN is used to run any command on top of image
RUN npm install
# it will install all the dependencies present in your project package.json file

# creating a user
RUN adduser -D Divyansh
# Set the user name or UID to use when running the image(by default is root)
# (cmd: docker run myimage whoami)
USER Divyansh

# ENV Set an environment variable to the specified value.
# cmd to check env var: docker run myimage env
ENV app_host='0.0.0.0'
ENV app_port=5000

# or
# ENV app_host='0.0.0.0' \
#     app_port=5000

# copy the contents of the current dir on your host machine into the working dir of the Docker image being built.
# cmd to check files: docker run myimage ls 
COPY . .
#copy single file
# COPY app.py .  

# used to copy files, directories, or remote URLs from your host machine or a URL into the filesystem of the Docker image being built.
ADD https://example.com/myfile.tar.gz .

# Define network ports for this container to listen on at runtime.
# docker inspect myimage
EXPOSE 3000

# used to specify the default command to be executed when a container is started from the Docker image.
# CMD [ "executable", "parameter", ... ]
CMD [ "npm" ,"start"]