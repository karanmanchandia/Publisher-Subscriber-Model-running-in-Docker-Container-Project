from flask import Flask, render_template, json, request, Response
from flaskext.mysql import MySQL

import urllib
import urllib2
import requests
import os

nodes = ["node1","node2","node3"]
this_node = os.environ['C_NAME'] # container name is docker address

nodes.remove(this_node)

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'phasetwo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/advertiseform')
def pre_create_channel():
    return render_template('advert.html')


@app.route('/advertise',methods=['POST'])
def create_channel():
    try:
        uuid = request.form['id']
        _name = request.form['name']

        # validate the received values
        if _name and uuid:
            
            # All Good, call MySQL
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM `client` WHERE `uuid` LIKE '{}'".format(uuid))
            data = cursor.fetchone()

            if data is None:
                cursor.execute("INSERT INTO `client` (`id`, `uuid`) VALUES (NULL, '{}')".format(uuid))
                conn.commit()
                cursor.execute("SELECT * FROM `client` WHERE `uuid` LIKE '{}'".format(uuid))
                data = cursor.fetchone()

            cursor.execute("INSERT INTO `chanel` (`id`, `client_id`, `name`) VALUES (NULL, '{}', '{}')".format(data[0], _name))
            conn.commit()

            # broadcast to other nodes
            global nodes
            data = urllib.urlencode(request.form)
            for node in nodes:
                url = node + "/advertise"
                req = urllib2.Request(url, data)
                response = urllib2.urlopen(req)

            return json.dumps({'message':'Channel created successfully !'})
        else:
            return json.dumps({'message':'All fields are required'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()

@app.route('/adverts_form', methods=['GET'])
def adverts_form():
    return render_template('adverts_form.html')

@app.route('/adverts', methods=['GET'])
def adverts_get():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT chanel.id, chanel.name, client.uuid FROM chanel INNER JOIN client ON chanel.client_id = client.id")
        data = cursor.fetchall()
        # return json.dumps(data)
        return Response(json.dumps(data), mimetype='application/json')

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()

@app.route('/create_event', methods=['POST', 'GET'])
def create_event():
    if request.method == 'GET':
        return render_template('creat_event_form.html')
    if request.method == 'POST':
        # broadcast to other nodes
        global nodes
        data = urllib.urlencode(request.values)
        for node in nodes:
            url = node + "/create_event"
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)

        chanel_id = request.values['chanel_id']
        description = request.values['event_description']

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO `event` (`id`, `chanel_id`, `description`) VALUES (NULL, '{}', '{}')".format(chanel_id, description))
        conn.commit()

        event_id = cursor.lastrowid

        # create notification for all subscribers of that channel
        cursor.execute("SELECT client_id FROM subscription WHERE chanel_id LIKE '{}'".format(chanel_id))
        data = cursor.fetchall()

        if data is not None:
            for subscription in data:
                cursor.execute("INSERT INTO notification (id, event_id, client_id) VALUES (NULL, '{}', '{}')".format(event_id, subscription[0]))
                conn.commit()
        
        return Response(json.dumps(data), mimetype='application/json')

@app.route('/my_chanels')
def my_chanels():
    uuid = request.args['uuid']

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT chanel.id, chanel.name, client.uuid FROM client INNER JOIN chanel ON chanel.client_id = client.id WHERE client.uuid LIKE '{}'".format(uuid)) 

    data = cursor.fetchall()

    return Response(json.dumps(data), mimetype='application/json')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        chanel_id = request.json['chanel_id']
        uuid = request.json['uuid']

        # broadcast to other nodes
        global nodes
        for node in nodes:
            url = node + "/subscribe"
            r = requests.post(url, json=request.json)

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM client WHERE uuid LIKE '{}'".format(uuid))
        data = cursor.fetchone()

        if data is None:
            cursor.execute("INSERT INTO `client` (`id`, `uuid`) VALUES (NULL, '{}')".format(uuid))
            conn.commit()
            cursor.execute("SELECT * FROM `client` WHERE `uuid` LIKE '{}'".format(uuid))
            data = cursor.fetchone()

        cursor.execute("INSERT INTO `subscription` (`id`, `client_id`, `chanel_id`) VALUES (NULL, '{}', '{}')".format(data[0], chanel_id))
        conn.commit()

        return json.dumps({'message':'Subscribed successfully !'})


    except Exception as e:
        return json.dumps({'error':str(e)})

@app.route('/notifications')
def render_notification_form():
    return render_template('notifications.html')

@app.route('/notify', methods=['GET'])
def notify():

    uuid = request.args['uuid']

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM client WHERE uuid LIKE '{}'".format(uuid))
    data = cursor.fetchone()


    if data is not None:
        notifications = []
        cursor.execute("SELECT event_id FROM notification WHERE client_id LIKE '{}'".format(data[0]))
        data = cursor.fetchall()

        if data is not None:
            for n in data:
                cursor.execute("SELECT event.description,chanel.name FROM event INNER JOIN chanel ON chanel.id=event.chanel_id WHERE event.id='{}'".format(n[0]))
                d = cursor.fetchone()

                notifications.append(d)
        return Response(json.dumps(notifications), mimetype='application/json')

if __name__ == "__main__":
    app.run()