# stable ubuntu image
FROM ubuntu:16.04

# python
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# MySQL
ENV MYSQL_PWD toor
RUN echo "mysql-server mysql-server/root_password password $MYSQL_PWD" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password $MYSQL_PWD" | debconf-set-selections
RUN apt-get -y install mysql-server
RUN apt-get install -y mysql-client
RUN apt-get install -y libmysqlclient-dev

# walkaround docker-mysql issues
RUN echo yes 
VOLUME ["/var/lib/mysql"]

RUN sed -i "s/127.0.0.1/0.0.0.0/g" /etc/mysql/mysql.conf.d/mysqld.cnf

RUN mkdir -p /var/run/mysqld
RUN usermod -d /var/lib/mysql/ mysql
RUN find /var/lib/mysql -type f -exec touch {} \;
RUN chown -R mysql:mysql /var/lib/mysql /var/run/mysqld

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME PhaseTwo

# Run app.py when the container launches
# CMD ["python", "app.py"]
ENV FLASK_APP app.py
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]