# Interacting with containers

A quick glossary of useful commands in the Docker CLI.

- `docker build` - Build an Image from a Dockerfile

- `docker run` - Run a Container of the desired Image

- `docker exec` - In a running container, execute a specific command

- `docker ps` - List all running containers

- `docker stop` - Stop a running container

- `docker start` - Restart a stopped container

In the left-hand menu of [Docker's documentation](https://docs.docker.com/engine/reference/commandline/cli/) you see all available commands. It's pretty big, so let's start with just the ones above :)

---

### Task 1 - Starting out

**Run Docker's Hello World**

Let's start simple, `docker run hello-world` is a tiny image which will just print some text.

**Try running the ubuntu container interactively**

Following the recommendation from hello-world, let's try `docker run -it ubuntu bash`.

Here, `-it` are required to start an interactive container, and `bash` is simply an instruction to run the bash command in ubuntu as we attach. If you want, see what happens when you omit them.

---

### Task 2 - Detaching

**Run a container in detached mode and list it**

Most of the time, you don't want/need an interactive terminal for your container. To detach you can use the run command it with `-d`.

Start a detached container with `docker run -d ubuntu sleep 30`. You can list all running containers with `docker ps`.

*Note, instead of `ubuntu sleep 30` you can use any other application image you like*

---

### Task 3 - Stop/Start

**Stop a container and restart it**

When starting a detached container, you will be presented with a Container ID. This is used to reference that specific container. Let's try stopping the detached container we started.

Use `docker stop [ID]`. Note that instead of copying the id, you can just write the first 4-5 characters.

Now, verify nothing is running in `docker ps`.

We can finally see the difference between Image and container! Use `docker container ls --all` to see all containers you have run. Every entry in this list is a unique container, based on the listed image.

Restart a stopped container again with `docker start [ID]`. It will start the same command we provided when we created the container with `docker run [image] [command]` (Or whatever predefined command the image was assigned).

---

### Task 4 - Attaching

**Attaching to a container**

Sometimes you need to attach a terminal to a specific container (running or previously run). Usually it's to check out file contents.

This can be done by using docker's exec command and opening a shell. The command will be `docker exec -it [ID] /bin/bash` or similar. Do note that not all containers come with bash, bust most do have sh.
