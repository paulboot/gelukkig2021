#!/bin/bash

while :
do
    /usr/local/bin/uwsgi --socket 0.0.0.0:5000 --wsgi-file myapp.py --callable app --processes 1 --threads 25 --stats 127.0.0.1:9191 >> /var/log/uwsgi.log 2>&1

    /usr/bin/sleep 2
done
