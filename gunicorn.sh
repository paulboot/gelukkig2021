#!/bin/bash

while :
do
   # /usr/local/bin/gunicorn --threads 5 --workers 1 --bind 0.0.0.0:5000 myapp:app >> /var/log/gunicorn.log 2>&1
   # /usr/local/bin/gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:5000 myapp:app >> /var/log/gunicorn.log 2>&1

    /usr/bin/sleep 2
done
