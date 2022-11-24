
from datetime import datetime


class Utilisateur():

    def __init__(self,
        id  = None,
        mail = None,
        prenom= None,
        nom= None,
        MDP= None,
        dateNaissance= None):

        self._id :int =id
        self._mail:str=mail
        self._MDP:str=MDP
        self._dateNaissance:str=dateNaissance
        self._nom:str = nom
        self._prenom:str = prenom


    @property
    def id(self):
        return self._id
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def prenom(self):
        return self._prenom
    @property
    def mail(self):
        return self._mail

    @property
    def MDP(self):
        return self._MDP

    @property
    def dateNaissance(self):
        return self._dateNaissance


    @mail.setter
    def mail(self, value):
        self._mail = value

    @MDP.setter
    def MDP(self, value):
        self._MDP = value

    @dateNaissance.setter
    def dateNaissance(self, value):
        self.dateNaissance = value