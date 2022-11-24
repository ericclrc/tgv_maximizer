from recherche.abstractrecherche import AbstractRecherche
from dao.db_connection import DBConnection
from dao.DAOtrajet import DAOTrajet
from dao.DAOhistorique import DAOHistorique
from datetime import datetime
import requests as rq

class RechercheTrajet(AbstractRecherche):
    
    def recherche(self,date, origine, destination, alerter : bool = False, eligible = "OUI"):

        
        origine_str = str(origine).replace(" ", "+")
        origine_str = origine_str.upper()
        destination_str = str(destination).replace(" ", "+")
        destination_str = destination_str.upper()

        date_obj = datetime.strptime(date, '%d/%m/%Y')
        jour = str(date_obj.day)
        mois = str(date_obj.month)
        annee = str(date_obj.year)

        url = "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&sort=-date&refine.origine=" + origine_str + "&refine.destination=" + destination_str + "&refine.date=" + annee + "%2F" + mois +  "%2F" + jour + "&exclude.od_happy_card=" + eligible
     
        
        dict1 = rq.get(url)
        dict2=dict1.json()
        datatest=[dict2["records"][k]for k in range(len(dict2["records"]))]
        data=[datatest[k]['fields'] for k in range(len(dict2["records"]))]
        for k in range(len(data)):
            print("Le train " + data[k]['train_no'] + " à destination de " + data[k]['destination'] + " partira de " + data[k]['origine'] + " à " +  data[k]['heure_depart'])
        return(url)

