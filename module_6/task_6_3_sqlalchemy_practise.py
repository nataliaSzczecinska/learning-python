# importing csv module
import csv
# importing sqlite3 module
import sqlite3
# importing sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

# read the csv file clean_stations
with open('clean_stations.csv', 'r') as csvfile:
    # create the object of csv.reader()
    csv_file_reader = csv.reader(csvfile, delimiter = ',')
    # skip the header
    next(csv_file_reader, None)
    # create fileds station, latitude, longitude, elevation, name, country, state
    station = ''
    latitude = ''
    longitude = ''
    elevation = ''
    name = ''
    country = ''
    state = ''

    ##### create a database table using sqlite3###

    # 1. create query to create clean_measure table
    table_clean_station_creation = '''CREATE TABLE if not Exists clean_stations 
    (station TEXT, latitude REAL, longitude REAL, elevation REAL, name TEXT, country TEXT, state TEXT)'''

    # 2. create database
    connection = sqlite3.connect('db_csv.db')
    curosr = connection.cursor()

    # 3. execute table query to create table
    curosr.execute(table_clean_station_creation)

    # 4. pase csv data
    for row in csv_file_reader:
        # skip the first row
        for i in range(len(row)):
            # assign each field its value
            station = row[0]
            latitude = row[1]
            longitude = row[2]
            elevation = row[3]
            name = row[4]
            country = row[5]
            state = row[6]

        # 5. create insert query
        InsertQuery = f"INSERT INTO clean_stations VALUES ('{station}','{latitude}','{longitude}','{elevation}','{name}','{country}','{state}')"

        # 6. Execute query
        curosr.execute(InsertQuery)
    # 7. commit changes
    connection.commit()
    # 8. close connection
    connection.close()


# read the csv file clean_measure
with open('clean_measure.csv', 'r') as csvfile:
    # create the object of csv.reader()
    csv_file_reader = csv.reader(csvfile, delimiter = ',')
    # skip the header
    next(csv_file_reader, None)
    # create fileds station,date,precip,tobs
    station = ''
    date = ''
    precip = ''
    tobs = ''

    ##### create a database table using sqlite3###

    # 1. create query to create clean_measure table
    table_clean_measure_creation = '''CREATE TABLE if not Exists clean_measure 
    (station TEXT, date TEXT, precip REAL, tobs INTEGER)'''

    # 2. create database
    connection = sqlite3.connect('db_csv.db')
    curosr = connection.cursor()

    # 3. execute table query to create table
    curosr.execute(table_clean_measure_creation)

    # 4. pase csv data
    for row in csv_file_reader:
        # skip the first row
        for i in range(len(row)):
            # assign each field its value
            station = row[0]
            date = row[1]
            precip = row[2]
            tobs = row[3]

        # 5. create insert query
        InsertQuery = f"INSERT INTO clean_measure VALUES ('{station}','{date}','{precip}','{tobs}')"

        # 6. Execute query
        curosr.execute(InsertQuery)
    # 7. commit changes
    connection.commit()
    # 8. close connection
    connection.close()

# SQLAlchemy
engine = create_engine('sqlite:///db_csv.db', echo = True)

print("TABLES IN DATABASE")
print(engine.table_names())

# select 5 stations
conn = engine.connect()
result = conn.execute("SELECT * FROM clean_stations LIMIT 5").fetchall()

print("Select first 5 stations")
print("station, latitude, longitude, elevation, name, country, state")
for i in result:
    print(i)

conn = engine.connect()
result = conn.execute("SELECT * FROM clean_measure LIMIT 5").fetchall()

print("Select first 5 measure")
print("station, date, precip, tobs")
for i in result:
    print(i)