import psycopg2
import requests
import gzip
import json
from dao.db_connection import DBConnection

from utils.singleton import Singleton
class DAOTrajet(metaclass=Singleton):

    def DAOTrajet(url):
        ### import d'un dictionnaire via l'API
        dict=requests.get(url)
        dict2=dict.json()
        datatest=[dict2["records"][k]for k in range(len(dict2["records"]))]
        data=[datatest[k]['fields'] for k in range(len(dict2["records"]))]
        conn=None
        cur=None
        try:
            ###Connexion au serveur 
            conn = DBConnection().connection
            cur = conn.cursor()
            ###Creation de la table
            create_script='''CREATE TABLE  IF NOT EXISTS trajet( date VARCHAR(40),
                                            origine VARCHAR(40),
                                            od_happy_card VARCHAR(40),
                                            train_no VARCHAR(40),
                                            heure_arrivee VARCHAR(40) ,
                                            axe VARCHAR(40) ,
                                            destination VARCHAR(40),
                                            entity VARCHAR(40),
                                            destination_iata VARCHAR(40) ,
                                            heure_depart  VARCHAR(40),
                                            origine_iata   VARCHAR(40)) '''
                                            
            cur.execute(create_script)
            ###Remplissage de la table
            for k in range(len(dict2["records"])):
                cur.execute('''INSERT INTO trajet (date,
                                            origine,
                                            od_happy_card,
                                            train_no,
                                            heure_arrivee,
                                            axe,
                                            destination,
                                            entity,
                                            destination_iata,
                                            heure_depart,
                                            origine_iata)'''\
                        '''VALUES (%(date)s,
                                            %(origine)s,
                                            %(od_happy_card)s,
                                            %(train_no)s,
                                            %(heure_arrivee)s,
                                            %(axe)s,
                                            %(destination)s,
                                            %(entity)s,
                                            %(destination_iata)s,
                                            %(heure_depart)s,
                                            %(origine_iata)s)''',
                        {"date": data[k]['date'],
                        "origine" : data[k]['origine'],
                        "od_happy_card": data[k]['od_happy_card'],
                        "train_no": data[k]['train_no'],
                        "heure_arrivee": data[k]['heure_arrivee'],
                        "axe": data[k]['axe'],
                        "destination": data[k]['destination'],
                        "entity": data[k]['entity'],
                        "destination_iata": data[k]['destination_iata'],
                        "heure_depart": data[k]['heure_depart'],
                        "origine_iata": data[k]['origine_iata']})
            conn.commit()
    
        except Exception as error : 
                print(error)
        finally : 
            ###déconnexion + arrêt curseur
                if cur is not None:
                    cur.close()
                if conn is not None :
                    conn.close()


