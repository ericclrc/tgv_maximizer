from typing import List, Optional

from utils.singleton import Singleton
from dao.db_connection import DBConnection
from utilisateur.utilisateur import Utilisateur


class DAOprofil(metaclass=Singleton):
    ######################## CHANGER DE MAIL ######################
    def changer_mail(self,user , nouveau_mail):
        request=  "UPDATE utilisateur "\
                    "SET mail=%(mail)s"\
                    " WHERE mdp=%(mdp)s RETURNING id_user "
        connection=DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                request,
                {"mail":nouveau_mail,
                "mdp": user.MDP
                })
            res = cursor.fetchone()
            if res :
                return True               


####################### CHANGER DE MOT DE PASSE #####################
    def changer_MDP(self,user , nouveau_mdp):
        request=  "UPDATE utilisateur "\
                    "SET mdp=%(mdp)s "\
                    "WHERE mail=%(mail)s RETURNING id_user "  
            
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:

                cursor.execute(
                    request,
                    {"mdp":nouveau_mdp,
                    "mail":user.mail
                    })
                res = cursor.fetchone()
                print(res)
        if res is not None :
            return True
        else :
            return False                 



###################### CREER SON COMPTE #####################
    def creer_compte(self,user: Utilisateur):
        created = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                create_script='''
                           CREATE TABLE IF NOT EXISTS utilisateur (
                                id_user SERIAL PRIMARY KEY NOT NULL,
                                
                                mail VARCHAR(50),
                                MDP VARCHAR(50),
                                dateNaissance VARCHAR(50),
                                nom VARCHAR(50),
                                prenom VARCHAR(50)
                                );'''
                                        
                cursor.execute(create_script)
                cursor.execute(
                    "INSERT INTO utilisateur (mail,MDP,dateNaissance, nom, prenom" \
                    ") VALUES (%(mail)s, %(MDP)s, %(dateNaissance)s, %(nom)s, %(prenom)s) RETURNING id_user"\
                    ,{
                    "MDP": user.MDP,
                    "mail": user.mail,
                    "nom": user.nom,
                    "prenom": user.prenom,
                    "dateNaissance": user.dateNaissance
                    })
                res = cursor.fetchone()
        if res:
            created = True
        else :
            created = False
        
        return created
        

            


###################### SE CONNECTER #####################
    def connexion(self,mail, MDP):
        user = Utilisateur()
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM utilisateur "\
                    "WHERE utilisateur.mail = %(mail)s AND utilisateur.MDP = %(mdp)s ",
                    {"mdp": MDP,
                    "mail": mail}
                    )
                res = cursor.fetchone()   
            
                 
        if res :
            user = Utilisateur(
                id  = res[0],
                mail = res[1],
                prenom= res[2],
                nom= res[3],
                MDP= res[4],
                dateNaissance= res[5]
            )
            return user
        else : 
            return(0)

                               



