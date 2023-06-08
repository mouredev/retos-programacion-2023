#!/bin/sh

HOST="mysql-5707.dinaserver.com"
PORT="3306"
USER="mouredev_read"
PASSWORD="mouredev_pass"
DATABASE="moure_test"

QUERY="SELECT * FROM challenges;"

mysql -h $HOST -u $USER -p$PASSWORD $DATABASE -e "$QUERY"