`cd /path/to/this/dir/`   

### Build image   
`$ docker build -t phase2 .`   

### Run image   
`$ docker run -p 8080:5000 phase2` 

### Start mysql
- in a different terminal window(don't use powershell)
run  
`$ docker ps `
take note of the latest *container_name*
run
`$  docker exec -it container_name /bin/bash `
the terminal prompt ill change to root@containerID:/app# 
start mysql service
`$ service mysql start` 
#### this is what was not happenig
then
`$ mysql -u root -ptoor < db.sql` 

open localhost:8080 in your browser

### Example Usage
# browser window 1
localhost:8080/advertiseform  Advertise
- enter user1 when prompted for UUID

# browser window 2
localhost:8080/adverts_form Subscribe
-  enter user2 when prompted for UUID

# browser window 2
localhost:8080/notifications Notifications
- open this in new browser window enter user2 when prompted for UUID

# browser window 1
localhost:8080/create_event New Event
- enter user1 when prompted for UUID
- each time you create an event it should apear in browser window 2


### Stack
- Flask 
web framework for interacting with sql database

- UI
jquery for sending and receiving data to server from client
bootstrap for pop up

the most important file is /templates/notifications.html
you'll find a javascript function called pollserver() it asks the server for notifications every 1000ms(1 second)