import os

class Settings:
    """ @author: Cesar Pabuena
        @version: v1 2025-04-09
        @funcionality: These are the aplication congifuration variables """

    HOST = os.getenv("HOST_IP")
    PORT = os.getenv("PORT_HOST")
    DEBUG = os.getenv("DEBUG")


    DB_USER = os.getenv("PG_USER")     #datos del .env
    DB_HOST = os.getenv("PG_HOST")
    DB_PASSWORD = os.getenv("PG_PASSWORD")
    DB_NAME = os.getenv("PG_NAME")
    DB_PORT = os.getenv("PG_PORT") 