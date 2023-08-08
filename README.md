# uw-wham-mdsplus

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

### MDSPlus Image
- This project includes a Dockerfile to build and create an MDSPlus docker image. The purpose of the MDSPlus docker image is to simplify the installation and setup of MDSplus to make it easier to get started with learning to use MDSPlus.
- Some useful links:
	- [Official MDSplus Docker project](https://github.com/MDSplus/Docker)
	- [Introduction to MDSplus using Docker](https://www.sciencedirect.com/science/article/pii/S0920379620306694)

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
- Subtrees are structured as a set of three MDSPlus files (.characteristics, .datafile, and .tree).
- Each subtree is stored in a separate directory under the `/data/wham_model/` directory. 
- NB: No two subtrees should share the same name. Indentical subtree names will result in conflicting paths and would make it difficult to restructure the tree later on (such as moving a subtree up a level)



### Merging Trees
- [Guide for merging trees in MDSPlus documentation](https://www.mdsplus.org/index.php/Documentation:Tutorial:CreateTrees)

### Environment
- Each tree in MDSPlus requires path environmental variable to be set with the name `<tree-name>_path`.
- In the case of the "wham" tree, the path variable is `wham_path`
- Subtrees follow a similar pattern. For example, the subtree for the RF system will have a path variable named `rf_path`. 
- The path variables for the trees are set in the directory `/etc/mdsplus.conf` This file is read by MDSPlus startup scripts on login. Tree path varibales **MUST** be setup here in order for them to show up in MDSPlus mdstcl or jTraverser.


### Naming Convention
- Tree and subtree names are limited to 12 characters.


### Configuring Data Directories
- [Tree Access](https://www.mdsplus.org/index.php/Documentation:TreeAccess)


### TCL


## MDSPlus Utilities

### mdstcl

### jTraverser

### jScope

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

