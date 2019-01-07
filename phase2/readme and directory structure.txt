                                              Emulating Pub/Sub Distributed System Using Docker Containers
                                                              Directory Structure and Readme
                                                                         Phase 2

Brief Project Discription:
This project aims to create a distributed Publish Subscribe Application that would disperse and propogate events to multiple users called subscribers through 
an intermediary. This intermediary can be called as a broker. In this project we will emulate Pub/Sub system using light weight virtulization or container 
technology in docker technology. In phase 2 of the project we will implement a centralized version of the pub/sub application.


Project Directory Structure:
The directory structure for phase 2 is shown below:

  Project Deliverables:
  1) Phase 2
         --Templates
		    --adverts.html
			--adverts_form.html
			--create _events_form.html
			--index.html
			--notifiations.html
         --app.py
		 --commands_to_run.md
		 --db.sql
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
   $ docker build -t phase2 .
8) Use the following command to run the image
   $ docker run -p 8080:5000 phase2
9) In the command prompt window (don't use powershell) run the command
   $ docker ps    
10) Take note of the latest *container_name*.
11) Run the command
    $  docker exec -it container_name /bin/bash
12) The terminal prompt will change to root@containerID:/app# 
13) Start my sql service by using the command
    $ service mysql start
14) Now run the command
    $ mysql -u root -ptoor < db.sql
15) Open localhost:8080 in your browser.

Example Usage:  

1) browser window 1  
localhost:8080/advertiseform  Advertise
- enter user1 when prompted for UUID

2) browser window 2  
localhost:8080/adverts_form Subscribe
-  enter user2 when prompted for UUID

3) browser window 2  
localhost:8080/notifications Notifications
- open this in new browser window enter user2 when prompted for UUID

4) browser window 1  
localhost:8080/create_event New Event
- enter user1 when prompted for UUID
- each time you create an event it should apear in browser window 2


