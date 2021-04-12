import mysql.connector
import time


def dataBase(vehicle_number, vehicle_type, allowed):
    # Create a connection object
    mydb = mysql.connector.connect(
        host="localhost",
        user="erez",
        password="123456",
        database="ereztest"
    )

    with mydb:
        with mydb.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `parking` (`vehicle_number`, `vehicle_type`, `allowed`, `timestemp`)" \
                  " VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (vehicle_number, vehicle_type, allowed, time.time()))

        mydb.commit()  # connection is not autocommit by default, so we must commit to save our changes.

        with mydb.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM parking ORDER BY id DESC LIMIT 1"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
