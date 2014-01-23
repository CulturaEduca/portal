#!/bin/bash
set -e
LOGFILE=/tmp/culturaeduca.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=nodeware
GROUP=nodeware
cd /home/nodeware/pyvirt/culturaeduca
source bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec bin/gunicorn_django -D -w $NUM_WORKERS -b unix:/tmp/culturaeduca.sock \
    --user=$USER --group=$GROUP --log-level=debug -p /tmp/culturaeduca.pid \
    --log-file=$LOGFILE 2>>$LOGFILE /home/nodeware/prod/culturaeduca

