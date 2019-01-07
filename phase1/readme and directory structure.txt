                                              Emulating Pub/Sub Distributed System Using Docker Containers
                                                              Directory Structure and Readme
                                                                         Phase 1

Brief Project Discription:
This project aims to create a distributed Publish Subscribe Application that would disperse and propogate events to multiple users called subscribers through 
an intermediary. This intermediary can be called as a broker. In this project we will emulate Pub/Sub system using light weight virtulization or container 
technology in docker technology. In phase 1 of the project we will create a web interface through which we can input a small program in python. The debug and 
Run button will load the program in Docker and execute it.


Project Directory Structure:
The directory structure for phase 1 is shown below:

  Project Deliverables:
  1) Phase 1
         --app.py
         --commands_to_run.md
         --Dockerfile
         --Readme and Directory Structure.txt
         --requirements.txt

How to Deploy and Run:
Below are the steps to deploy and run the code files for Phase1 of the project:

1) Follow the steps given on the link https://docs.docker.com/toolbox/toolbox_install_windows/ to install docker toolbox on your windows system.
2) Follow the steps given on the link https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1 to install docker on your Ubuntu system.
   [ Note that virtulization should be enabled in the BIOS settings in order for Docker to work.]
3) Verify that Docker toolbox is installed correctly by running the hello-world image using the command:
   $ docker run hello-world
4) Hello from Docker!
   This message shows that your installation appears to be working correctly.
5) Open Docker Quickstart Terminal by clicking the icon on the desktop.
6) cd /path/to/this/dir/ to the phase 1 directory. 
7) Run the following command to build a docker image
   $ docker build -t phase1 .
8) Use the following command to run the image
   $ docker run -p 8080:8888 phase1
11) Open localhost:8080 in your browser.
12) Type your python program in the textbox.
13) Click on Debug and Run button.
14) The python program will run in the docker container and output will be displayed on the screen. 


