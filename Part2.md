# Building an Image

In part 2, we will write a Dockerfile and experiment with some common operations such as port exposure and volume-mounting.

### Task 1: Create a Docker Image

In the `application` folder of this repo, there is a tiny application which launches an API with a single endpoint: `/content`. The app is written in Python, using FastAPI. To build a Dockerfile for this app you need to do the following:

1. Use **FROM** to choose base image
2. Use **RUN** to create a new folder with `mkdir`
3. Use **WORKDIR** to define the working directory of the image
4. **COPY** the files used by the application
5. **RUN** the package installation with `pip install -r requirements.txt`
6. Use **CMD** to choose startup command for the Container

Check [docker.io](https://index.docker.io/_/python?tab=description) to see the list of available python base images. I recommend `python:3.10-slim`.

Check [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) for more info on how to use the commands.

The command we want to run to start the API is: `uvicorn path.to.app:app --host 0.0.0.0`

Using the above information, write a `Dockerfile`. To build your Image, use `docker build . -t [image-name]`, and to run it `docker run [image-name]`.

### Task 2: Ports?

When the container is running, we want to access the application. The application output says it's listening on port 8000, but going to `localhost:8000` will not connect to the API.

We need to *publish* the container port to the host machine. It can be done by adding the flag `-p [host-port]:[container-port]` to the docker run command.

Another method is to *expose* the port in the Dockerfile. Adding `EXPOSE 8000` to the Dockerfile tells the user that the 8000 port is the application port in the image. Publishing the exposed port is done by adding only the host port into the flag: `-p [host-port]`.

Try both methods, to make sure the API is accessible from localhost! Try using host-ports other than 8000.

### Task 3: Hot reloading inside containers

Some frameworks (mostly in python and javascript-land) have a feature for hot-reloading your code. To use hot-reloading for FastAPI we can add `--reload` to the uvicorn command. Of course, this won't work if you're running it with a container.

This is one of many use-cases of volumes. 

Mount application folder contents as a volume and try hot-reloading from a container.
