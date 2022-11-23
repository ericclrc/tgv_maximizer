from abc import ABC, abstractmethod

class AbstractRecherche(ABC):

    @abstractmethod
    def recherche(self):
        """Méthode abstraite de recherche""" 