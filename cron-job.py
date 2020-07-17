#!/usr/bin/python3
import psycopg2
from  datetime import datetime
import os 

connection = psycopg2.connect("dbname=file_storage user=postgres password=password");
cursor = connection.cursor();
current_time = datetime.now();

selectStatement     = f"SELECT * FROM file where file.expiration_time < '{current_time}'";
cursor.execute(selectStatement);
rows = cursor.fetchall();

for row in rows:
    os.remove(os.path.join(os.path.dirname(__file__), 'data', str(row[0])));

deleteStatement     = f"DELETE FROM file where file.expiration_time < '{current_time}'";
cursor.execute(deleteStatement);
connection.commit();

cursor.close();
connection.close();