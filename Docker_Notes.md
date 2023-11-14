## MDSplus Docker

### Docker Introduction
- Docker is a platform that enables you to develop, package, and deploy software within isolated environments called **containers**. 
- Containers are lightweight and portable, allowing applications to run consistently across different computing environments.

#### Key Concepts:
1. **Container:** A standalone unit encapsulating an application and its dependencies. Containers are isolated from each other and the host system, ensuring consistent and interference-free operation.
2. **Image:** A read-only blueprint used to create containers. It contains application code, runtime, libraries, and settings. Images are stored in a **registry**, a repository for sharing and distributing images.
3. **Dockerfile:** A text file with build instructions for creating a Docker image. Defines the base image, software packages, application code, and configurations.
4. **Docker Engine:** Core Docker component managing containers. Includes a server, REST API, and CLI for container management. There is also an alternative engine called Podman which can be used on Linux machines
5. **Registry:** Repository for storing and distributing Docker images. Docker Hub is a popular public registry with many public base images available. Alternatively, privately hosted registries offer secure image storage. 
6. **Entrypoint:** A bash script that is executed upon startup of a container.

#### Benefits:
- **Portability:** Containers run consistently across environments, reducing compatibility issues and facilitating application movement.
- **Isolation:** Containers provide process and file system isolation, preventing interference with each other and the host system.
- **Resource Efficiency:** Containers share the host OS kernel, resulting in efficient resource utilization compared to traditional virtual machines.
- **Rapid Deployment:** Docker enables quick, consistent application deployment, reducing setup and configuration time.
- **Version Control:** Docker images and Dockerfiles allow versioning of application components, simplifying change tracking and rollback.

#### Docker Documentation

### MDSPlus Image
- This project includes a Dockerfile to build and create an MDSPlus docker image. The purpose of the MDSPlus docker image is to simplify the installation and setup of MDSplus to make it easier to get started with learning to use MDSPlus.
- The MDSplus docker image in this project is built on top of Ubuntu Linux. You can look through the Dockerfile to see how MDSplus is installed and configured. Many of the installation steps were found using trial and error since the MDSplus documentation is not regularly updated.
- There is also an [official MDSplus Docker project](https://github.com/MDSplus/Docker) that is built on top of Alpine Linux. At the time of writing (August 2023) there were errors running the container
- Some useful links:
	- [Official MDSplus Docker project](https://github.com/MDSplus/Docker)
	- [Introduction to MDSplus using Docker](https://www.sciencedirect.com/science/article/pii/S0920379620306694)

#### Building the Image
- Naviagate to the directory containing the Dockerfile
- Run `docker build -t mdsplus .`
- If you encounter errors, it can sometimes be resolved by building with the `--no-cache` argument: `docker build --no-cache -t mdsplus .`


#### Setup X11 Forwarding (Optional)
- This step is optional and only necessarily if you are using a graphical program such as jTraverser from within the container
- Confirmed working on MacOS. X11 has not been tested on Linux or Windows but it should be possible.
- MacOS:
	- Install [XQuartz](https://www.xquartz.org/)
	- Launch XQuartz. Go to the XQuartz menu and open Preferences. 
	- Go to the security tab and enable "Allow connections from network clients".
	- From a terminal window, run `xhost + ${hostname}`
	- Set `export HOSTNAME=`hostname``
	- [GitHub discussion about X11 forwarding (link)](https://gist.github.com/cschiewek/246a244ba23da8b9f0e7b11a68bf3285)
	

#### Running the Container
- Command to startup the container as an interactive session: `docker run --rm -it -e DISPLAY=host.docker.internal:0 -v /tmp/.X11-unix:/tmp/.X11-unix -v /Users/cameron/Projects/uw-wham-mdsplus/mdsplus_docker/my_tree:/mytree mdsplus:latest /bin/bash`
	- Arguments:
		- `-rm`: Removes the container when you exit the session. Any changes to files within the container will be lost unless you write them to a shared volume or directory on the host.
		- `-it`: Starts contianer as an interactive session rather than a process in running in the background.
		- `-e DISPLAY=host.docker.internal:0`: Sets the `DISPLAY` environmental variable within the container for the X11 forwarding.
		- `-v /tmp/.X11-unix:/tmp/.X11-unix`: Creates shared volume between the host and the container for an X11 socket.
		- `-v /Users/cameron/Projects/uw-wham-mdsplus/mdsplus_docker/my_tree:/mytree mdsplus:latest`: Creates a shared volume between the host and the contianer. The format is `host_dir:container_dir`. 
		- `/bin/bash`: Command to run immediately after launching the container. In this case, a bash session is opened.

#### Dockerfile


#### Entrypoint


#### mdsplus.conf