#!/bin/bash

host="mysql-5707.dinaserver.com"
port="3306"
user="mouredev_read"
database="moure_test"

query="SELECT * FROM challenges"

result=$(echo "$password" | mysql -h "$host" -P "$port" -u "$user" -p "$database" -e "$query")

if [ $? -ne 0 ]; then
    echo "Error al ejecutar la consulta"
    exit 1
fi

echo "$result"

