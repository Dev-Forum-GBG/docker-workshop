# Introduction to Docker

Docker popularized running software in containers which is an important piece of technology that has enabled us to put our services in the cloud instead of managing servers in the office closet.

## What is a Container?

At first glance, a container looks like a virtual machine, running its own operating system and any applicstions you put in it.

Try running a container, and you will immediately see that they are much more lightweight, and start up in almost no time. What's up with that?

A container is a loosely isolated environment containing everything you need to run your application. This decouples the application from the machine it is running on, and allows us to run our application anywhere! The application will behave the same on your machine, in the cloud, or wherever you run the container.

## Containers and Images?

One initially confusing part of getting started with Docker is the vocabulary. There are plenty of new concepts to dive into, but we will start the one of the most common sources of confusion: Image vs Container.

`A Dockerfile defines what an Image should contain`

`An Image is a blueprint for starting a Container`

`Containers are the running application`

When you `build` a Dockerfile, you create an Image which contains all the required information and files to start a Continer.

When you `run` an Image, it starts the container with the information and files built into the Image.

You can have multiple Containers from the same Image running at once.

## Why Containers?

Three reasons for using containers:

### 1. Reproducible & Self-Contained

Packaging your application in an image forces you as a dev to include all of its dependencies in the image. This little extra work ensures the application is the same when run on your machine as it is when running in the cloud.

### 2. Distribution & Deployment

Since everything needed to run your application is packaged in the image, dpeloyment and distribution become much simpler. There's no need to install dependencies or libraries, and you can replace your container with a newer version in seconds.

### 3. Scaling

Scaling a containerized application is simple, you just start up another container! It does however require you to design your application in a scalable manner (which is good practice anyways).

## On security

Just a little note on Security. Downloading an Image from the internet should be regarded as downloading an appliction. Only use trusted sources.

[Read more](https://docs.docker.com/get-started/overview/)
