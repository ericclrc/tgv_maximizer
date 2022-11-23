import os

import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from utils.singleton import Singleton


class DBConnection(metaclass=Singleton):
    """
    Technical class to open only one connection to the DB.
    """
    def __init__(self):
        dotenv.load_dotenv(override=True)
        # Open the connection. 
        self.__connection =psycopg2.connect(
            host="sgbd-eleves.domensai.ecole",
            port="5432",
            dbname="id1994",
            user="id1994",
            password="id1994",
            cursor_factory=RealDictCursor)

    @property
    def connection(self):
        """
        return the opened connection.

        :return: the opened connection.
        """
        return self.__connection