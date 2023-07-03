from peewee import *

database = MySQLDatabase('fastapi_project',
                         user="root",
                         password="root",
                         host="localhost",
                         port=3306)