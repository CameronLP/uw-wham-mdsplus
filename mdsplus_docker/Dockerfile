FROM ubuntu:jammy
LABEL maintainer="Cameron Penne <cameron.l.penne@ntnu.no>"

# Update repo list
RUN apt-get update

# Install utilities
RUN apt-get -y install bash
RUN apt-get -y install x11-apps \
						curl \
						wget \
						nano \
						gnupg \
						libreadline-dev

# Add MDSPlus repository so Ubuntu can install MDSPlus

# Get repo key
#RUN curl -fsSL http://www.mdsplus.org/dist/mdsplus.gpg.key | apt-key add -

# Add MDSPlus repo to list
#RUN echo 'deb [arch=amd64] http://www.mdsplus.org/dist/Ubuntu22/repo MDSplus stable' > /etc/apt/sources.list.d/mdsplus.list

# Create keyrings directory for MDSPlus repo key
RUN mkdir -p /etc/apt/keyrings/

# Get repo key and move to keyrings directory
RUN wget http://www.mdsplus.org/dist/mdsplus.gpg.key && mv ./mdsplus.gpg.key /etc/apt/keyrings/ 

# Add repo and key to repo sources list
RUN echo "deb [signed-by=/etc/apt/keyrings/mdsplus.gpg.key] http://www.mdsplus.org/dist/Ubuntu22/repo MDSplus stable" > /etc/apt/sources.list.d/mdsplus.list

# Update repo list AFTER adding MDSPlus repo
RUN apt-get update

# Install MDSPlus prereqs
RUN apt-get -y install python3-numpy 
RUN apt-get -y install openjdk-8-jre
RUN apt-get -y install libxm4 libuil4 libmrm4 libmotif-common
RUN apt-get -y install python3-pip
RUN pip3 install pyxml3

# Install MDSPlus
RUN apt-get -y install mdsplus
RUN apt-get -y install mdsplus-kernel
RUN apt-get -y install mdsplus-python
RUN apt-get -y install mdsplus-java
RUN apt-get -y install mdsplus-motif
RUN apt-get -y install mdsplus-rfxdevices
RUN apt-get -y install mdsplus-mitdevices
RUN apt-get -y install mdsplus-camac 
RUN apt-get -y install mdsplus-hdf5
RUN apt-get -y install mdsplus-mssql 



# Copy MDSPlus Tutorials
RUN wget -O - https://github.com/MDSplus/MDSplusTutorial/archive/master.tar.gz | tar zxf -

# Configure environment for MDSPlus
# Copy everything to /root/.bashrc so environment is set for root user on log in
# From the documentation here: https://www.mdsplus.org/index.php?title=Documentation:Tutorial:CreateTrees&open=18815532534152659725254719&page=Tutorials%2FTrees+%26+Data
#/usr/local/mdsplus/lib/libJavaMds.so
RUN echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/mdsplus/lib/" >> /root/.bashrc
RUN echo "export PATH=$PATH:/usr/local/mdsplus/bin/" >> /root/.bashrc
RUN echo "export MDS_PATH=/usr/local/mdsplus/tdi/" >> /root/.bashrc
RUN echo "export CLASSPATH=$CLASSPATH:/usr/local/mdsplus/java/classes/jScope.jar:/usr/local/mdsplus/java/classes/jTraverser.jar:/usr/local/mdsplus/java/classes/jDevices.jar:/usr/local/mdsplus/java/classes/MDSobjects.jar:/usr/local/mdsplus/java/classes/jDispatcher.jar" >> /root/.bashrc
RUN echo "export MDSPLUS_DIR=/usr/local/mdsplus/" >> /root/.bashrc
RUN echo "export PyLib=python3.10" >> /root/.bashrc
RUN echo "export MDSPLUS_DIR=/usr/local/mdsplus/" >> /root/.bashrc
RUN echo "export MDS_PYDEVICE_PATH=/usr/local/mdsplus/pydevices/" >> /root/.bashrc

# Create command aliases for jTraverser and jScope to make them easier to call
RUN echo "alias jTraverser='java -jar /usr/local/mdsplus/java/classes/jTraverser.jar'" >> /root/.bashrc
RUN echo "alias jScope='java -jar /usr/local/mdsplus/java/classes/jScope.jar'" >> /root/.bashrc



RUN pip3 install matplotlib
RUN pip3 install h5py
RUN pip3 install django
RUN pip3 install xarray



# Copy files into container
COPY envsyms /usr/local/mdsplus/local/envsyms
COPY entrypoint.sh /entrypoint.sh

# Set entrypoint script for container
ENTRYPOINT ["/entrypoint.sh"]
