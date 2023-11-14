# UW WHAM MDSplus Documentation

## Introduction
- 



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

## Copy from `andrew`
- scp -r WHAMdata@andrew.psl.wisc.edu:/data/wham_model/pydevices ~/Desktop/
