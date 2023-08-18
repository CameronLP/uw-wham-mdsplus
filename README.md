# UW WHAM MDSplus Documentation

## Introduction
- 

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

## MDSPlus Concepts


### Tree
- Trees are structured as a set of three MDSplus files (.characteristics, .datafile, and .tree).
- The top node in the tree is stored in the `/data/wham_model/top/` directory. 

### Node


### Structure


### Subtrees
- Subtrees are structured as a set of three MDSplus files (.characteristics, .datafile, and .tree).
- Each subtree is stored in a separate directory under the `/data/wham_model/` directory. 
- Even though trees can be nested in the MDSplus tree database, the actual MDSplus files (.characteristics, .datafile, and .tree) are stored in a flat (single level) directory structure.
- **NB:** No two subtrees should share the same name. Indentical subtree names will result in conflicting paths and would make it difficult to restructure the tree later on (such as moving a subtree up a level).



### Merging Trees
- [Guide for merging trees in MDSPlus documentation](https://www.mdsplus.org/index.php/Documentation:Tutorial:CreateTrees)

### Environment
- Each tree in MDSPlus requires path environmental variable to be set with the name `<tree-name>_path`.
- In the case of the "wham" tree, the path variable is `wham_path`
- Subtrees follow a similar pattern. For example, the subtree for the RF system will have a path variable named `rf_path`. 
- The path variables for the trees are set in the directory `/etc/mdsplus.conf` This file is read by MDSPlus startup scripts on login. Tree path varibales **MUST** be setup here in order for them to show up in MDSPlus mdstcl or jTraverser.
- [Section: A Quick Check for some important environment variables](https://www.mdsplus.org/index.php?title=Documentation:Tutorial:CreateTrees&open=18815532534152659725254719&page=Tutorials%2FTrees+%26+Data)


### Naming Convention
- Tree and subtree names are limited to 12 characters.


### Configuring Data Directories
- [Tree Access](https://www.mdsplus.org/index.php/Documentation:TreeAccess)


### TCL

### TDI

### Shots


## MDSPlus Utilities

### mdstcl

### jTraverser

### jScope




## WHAM MDSplus Tree

### Summary


### Accessing the WHAM tree
- SSH as user `WHAMdata` (case sensitive) to [andrew.physics.wisc.edu](andrew.physics.wisc.edu).
- Use `jTraverser` or `mdstcl` to inspect or modify the model tree (shot number -1)


### Tree Structure
- The main top level tree is named `wham`. Beneath the top level, there are several subtrees.
- Subtrees are organized by system:
	- `BIAS` for the biasing system
	- `DIAG` for the diagnostics system
	- `ECH` for electron cyclotron heating system
	- `MISC` for miscellaenous items
	- `NBI` for the neutral beam injector system
	- `RF` for the radio frequency system
- Each system subtree is divided into two primiary parts: a processing structure and a raw data subtree.
	- `_RAW`: The raw data subtree follows the naming convention of `<system-name>` + `_RAW`. It contains any nodes or subtrees involved in collecting raw, unprocessed data from sensors or instruments. Each raw data subtree exists as an entirely separate set of tree files (.characteristics, .datafile, and .tree) that has been merged with the system subtree.
	- `_PROC`: The processing stucture follows the naming convention of `<system-name>` + `_PROC`. It contains any nodes or subtrees responsible for processing the raw data using TDI expressions. The processing structure does not exist as a separate tree; instead it is an inherent part of the parent system subtree.
	- `_PARAMS_`: The parameters stucture follows the naming convention of `<system-name>` + `_PARAMS`. It contains any nodes used to hold parameters or constants used by the `_PROC` nodes. The parameters structure does not exist as a separate tree; instead it is an inherent part of the parent system subtree.
- The main structure of the WHAM MDSplus tree was based off of the MDSplus tree created for the Madison Symmetric Torus (MST). This was done to adopt the good practices from the MST. However, there are several differences present in the WHAM MDSplus:
	1. In the MST MDSplus tree, subtrees begin with the prefix `mst_`. This style of naming convention was not adopted for the WHAM tree since subtree names can quickly run into the 12 character limit.
	2. Each system subtree is divided into two primiary parts: a processing structure and a raw data subtree. This organizes and separates the raw data from processed data while still allowing systems to be selectively enabled or disabled during shots. Additionally, because each raw data subtree exists as a distinct tree from their parent system subtrees, file permissions can be configured to protect recorded raw data.





## MDSPlus Documentation
- Recommended reading:
	- [Tutorials](https://www.mdsplus.org/index.php?title=Documentation:Tutorial&open=18815634063302659165716529&page=Documentation%2FTutorials)
	- [Basic Concepts](https://www.mdsplus.org/index.php?title=Documentation:Tutorial:QuickOverview&open=1624466399993193889855&page=Tutorials%2FQuick+Tour)
	- [The Data Hierarchy - Trees, Nodes, and Models](https://www.mdsplus.org/index.php?title=Documentation:Tutorial:CreateTrees&open=18815532534152659725254719&page=Tutorials%2FTrees+%26+Data)
	- [OOP Interface (including Python)](https://www.mdsplus.org/index.php?title=Documentation:Tutorial:MdsObjects&open=38101832318169843162415089&page=Documentation%2FThe+MDSplus+tutorial%2FThe+Object+Oriented+interface+of+MDSPlus)
	- [Experimental Sequence](https://www.mdsplus.org/index.php?title=Documentation:Tutorial:ExperimentSequence&open=38101832318169843162415089&page=Documentation%2FThe+MDSplus+tutorial%2FSetting+up+an+experiment+sequence)
	- [Devices](https://www.mdsplus.org/index.php?title=Documentation:Tutorial:Devices&open=38101832318169843162415089&page=Documentation%2FThe+MDSplus+tutorial%2FDeveloping+MDSplus+devices)
- MDSplus quick reference
	- [Tree Command Language (TCL)](https://www.mdsplus.org/index.php?title=Documentation:Reference:TCL_index&open=18815634135359153558782001&page=Documentation%2FReference%2FTCL)
	- [TDI](https://www.mdsplus.org/index.php?title=Documentation:Reference:TDI&open=18815634135359153558782001&page=Documentation%2FReference%2FTDI)
	- []()
	
## Setting Up Devices on `andrew.physics.wisc.edu`
- `export MDS_PYDEVICE_PATH=/data/wham_model/pydevices`
- `export PYTHONPATH=$PYTHONPATH:/data/wham_model/pydevices` or `export PYTHONPATH=/home/WHAMdata/MDSplus/:/data/wham_model/pydevices`
- Anaconda (not recommended): `export PyLib=/home/WHAMdata/anaconda3/lib/libpython3.8.so`
- System Python: `export PyLib=/usr/lib64/libpython3.so`
- Devices files are placed in `/data/wham_model/pydevices/`. This should be changed to `/usr/local/mdsplus/pydevices` (requires sudo).
- The Python shared library `libpython3.8.so` is weird to setup since it is part of an Anaconda installation of Python. Might be wise to change this to a system installation of Python depending on how Python scripts for MDSplus are run. Also need to be aware of an updated that require the path to the `.so` file to be changed.
- Once sudo access is obtained, make sure to remove the two `export` commands from above in the `~/.bashrc` file


## Finding Current Shot
- Using Python:
```
from MDSplus import *
t = Tree("wham", -1)
s = t.getCurrent()
print(s)
```
- Using Python from a **remote** machine:
```
from MDSplus import connection
c = connection.Connection("andrew")
c.openTree("wham", 0)
s = c.get('$shot')
print(s)
```

## Editting Tree
- Using TCL:
```
edit my_tree
delete node RP/confirm
add node RP/model=WHAM_RED_PITAYA_FAKE
write
close
exit
```


## Taking Test Shot
- Using TCL:
```
set tree my_tree /shot=-1
set current my_tree /increment
create pulse 0
set tree my_tree /shot=0
dispatch /build
dispatch /phase INIT
```


## Checking Data in Device
- Using Python:
```
from MDSplus import *
t = Tree("my_tree", 3)
c = t.RP.getNode(":CH_01")
```

## Accessing MDSplus Data Remotely
- Using Python:
```
from MDSplus import connection
conn = connection.Connection("andrew.psl.wisc.edu")
conn.openTree("wham",0)
conn.get("ECH.ECH_RAW.RP_1:CH_01")
```


## Other
- docker run --rm -it -p 8000 -e DISPLAY=host.docker.internal:0 -v /tmp/.X11-unix:/tmp/.X11-unix -v /Users/cameron/Projects/uw-wham-mdsplus/mdsplus_docker/my_tree:/my_tree -v /Users/cameron/Projects/WHAM_Data/:/WHAM_Data/ mdsplus:latest /bin/bash

## Plotting
- [MDSmonkey in Python](https://github.com/lamorton/MDSmonkey)