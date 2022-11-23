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
        # Open the connection. 
        self.__connection =psycopg2.connect(host='localhost',

                        dbname = 'tgv_max',
                        user = 'postgres',
                        password = 'Ericlulu2805*',
                        port = 5432)

    @property
    def connection(self):
        """
        return the opened connection.

        :return: the opened connection.
        """
        return self.__connection