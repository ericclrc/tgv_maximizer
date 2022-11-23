from utilisateur.utilisateur import Utilisateur
import psycopg2
from dao.db_connection import DBConnection
from utils.singleton import Singleton

class DAOHistorique():
    def remplir(type, date, origine, destination, eligible, alerter):
        conn=None
        cur=None
        try:
            ###Connexion au serveur 
            conn=DBConnection().connection
            cur = conn.cursor()
            create_script='''CREATE TABLE  IF NOT EXISTS historique (type VARCHAR(40),
                                                                    id_util INT,
                                                                    date VARCHAR(40),
                                                                    origine VARCHAR(40),
                                                                    destination VARCHAR(40),
                                                                    eligible VARCHAR(40),
                                                                    alerter VARCHAR(40))'''
            cur.execute(create_script)
            cur.execute('''INSERT INTO historique(type, date, origine, destination,
                                                   eligible, alerter)'''\
                        '''VALUES(%(type)s,
                                    %(date)s,
                                    %(origine)s,
                                    %(destination)s,
                                    %(eligible)s,
                                    %(alerter)s)''',
                        {"type": type,
                        "date" : date,
                        "origine" : origine,
                        "destination" : destination,
                        "eligible" : eligible,
                        "alerter" : alerter
                        })
            conn.commit()
        except Exception as error : 
                print(error)
        finally : 
            ###déconnexion + arrêt curseur
                if cur is not None:
                    cur.close()
                if conn is not None :
                    conn.close()



