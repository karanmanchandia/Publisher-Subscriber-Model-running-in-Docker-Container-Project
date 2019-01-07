# Intro
I have slightly modified the code so that each time some 
information is sent to a node , it is replayed to the other nodes,
this is the flooding technique discussed in colouris text.

I created three containers such that when someone connects to one container and another 
connects to the others a message is sent to the other two

# Set Up 

The set up might take some time depending on your internet connection
`
$ docker-compose build
$ docker-compose up
`

cointainer1: localhost:4001
cointainer2: localhost:4002
cointainer3: localhost:4003

## Start mysql 
`$ docker ps `
take note of the three latest *container_name*
`$  docker exec -it container_name /bin/bash `
this command is used to login to a container
a container is like an ubuntu computer/server
the terminal prompt will change to root@containerID:/app# 
`$ service mysql start` 
`$ mysql -u root -ptoor < db.sql` 

run these three commands for the three container_name


# Example Usage
### browser window 1
localhost:4001/advertiseform  Advertise
- enter user1 when prompted for UUID

### browser window 2
localhost:4002/adverts_form Subscribe
-  enter user2 when prompted for UUID

### browser window 3
localhost:4003/notifications Notifications
- open this in new browser window enter user2 when prompted for UUID

### browser window 1
localhost:4001/create_event New Event
- enter user1 when prompted for UUID
- each time you create an event it should apear in browser window 3



ask me any questions before 3 pm your local time