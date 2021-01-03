#!/bin/bash

while :
do
    /usr/local/bin/rq worker microbit >> /var/log/rq.log 2>&1

    /usr/bin/sleep 2
done
