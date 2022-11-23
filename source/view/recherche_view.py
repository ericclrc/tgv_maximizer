"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
From : https://github.com/CITGuru/PyInquirer/blob/master/examples/checkbox.py
"""
from pprint import pprint

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from prompt_toolkit.validation import Validator, ValidationError
from view.abstract_view import AbstractView
from view.session import Session
from recherche.recherchedestination import RechercheDestination
from recherche.recherchetrajet import RechercheTrajet
from recherche.rechercheweekend import RechercheWeekend

from dao.DAOtrajet import DAOTrajet

DEPART_SELECTION = inquirer.text(
            message="Votre gare de départ: ")

ARRIVEE_SELECTION = inquirer.text(
            message="Votre gare d'arrivée")

DATE_SELECTION = inquirer.text(
            message="Choisir votre date de départ (sous forme dd/mm/yyyy): ")
ALERTE_SELECTION = inquirer.checkbox(message='Etre alerté?', choices=[
                Choice('OUI')
                ,Choice('NON')
            ]
)
ELIGIBLE = inquirer.checkbox(
            message="Places eligibles au TGVMax? "
            ,choices=[
                Choice('OUI')
                ,Choice('NON')
            ]
)


class RechercheView(AbstractView):
    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Bonjour {Session().user.nom}, vous cherchez des trajets: '
            , choices=[
                Choice('''Recherche d'un Trajet ''')
                ,Choice('Des destinations atteignables durant un weekend'),
                Choice('Destinations disponibles depuis votre gare')
                ]
        )
        
    def display_info(self):
        print(f"Hello {Session().user.nom}, veuillez saisir vos critères")

    def make_choice(self):
        response = self.__questions.execute()

        if response == '''Recherche d'un Trajet ''':
            depart = DEPART_SELECTION.execute()
            arrivee = ARRIVEE_SELECTION.execute()
            date = DATE_SELECTION.execute()
            alerter = ALERTE_SELECTION.execute()
            eligible = ELIGIBLE.execute()
            resultat = RechercheTrajet.recherche(date=date,origine=depart,destination=arrivee,alerter=alerter,eligible=eligible)

        elif response== 'Des destinations atteignables durant un weekend':
            depart = DEPART_SELECTION.execute()
            arrivee = ARRIVEE_SELECTION.execute()
            date = DATE_SELECTION.execute()
            alerter = ALERTE_SELECTION.execute()
            eligible = ELIGIBLE.execute()
            resultat = RechercheWeekend.recherche(date,depart, arrivee, alerter, eligible)
        
        elif response=='Destinations disponibles depuis votre gare':
            depart = DEPART_SELECTION.execute()
            date = DATE_SELECTION.execute()
            alerter = ALERTE_SELECTION.execute()
            eligible = ELIGIBLE.execute()
            resultat=RechercheDestination.recherche(date,depart,alerter,eligible)


        # si aucun trajet ne correspond pas aux critères
        if not resultat:
        
            print('No results')
            # Demander si il veut creer un alerte?
            alerte = False
            alerte = inquirer.confirm(message="Voulez-vous être alerté par email quand une place remplissant vos critères de recherche se libère? (oui/non)",
                                            confirm_letter="oui", reject_letter="non", 
                                            default=True).execute()
            if alerte:
                DAOrecherche.add_recherche()

            proceed = False
            proceed = inquirer.confirm(message="Continuer votre recherche? (oui/non)",
                                            confirm_letter="oui", reject_letter="non", 
                                            default=True).execute()
            if proceed:
                return RecherchView()
            else: 
                from view.choix_view import ChoixView
                return ChoixView()

