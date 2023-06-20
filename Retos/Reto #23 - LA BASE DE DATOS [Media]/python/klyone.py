#!/usr/bin/env python3

import mysql.connector

def connect_bd():
    bd_connection = mysql.connector.connect(host = "mysql-5707.dinaserver.com", user = "mouredev_read", password = "mouredev_pass", database = "moure_test")
    return bd_connection

def get_bd_requester(bd_connection):
    requester = bd_connection.cursor()
    return requester

def query(requester, cmd):
    requester.execute(cmd)

def print_query_results(requester):
    result = requester.fetchall()
    for r in result:
        print(r)

if __name__ == "__main__":
    bd = connect_bd()
    requester = get_bd_requester(bd)
    query(requester, "SELECT * FROM challenges")
    print_query_results(requester)
