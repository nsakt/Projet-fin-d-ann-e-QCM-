import os
import random

class Question :

    """Classe pour question"""

    def __init__ (self) :
        self.enonce = None
        self.repa = None
        self.repb = None
        self.repc = None
        self.repd = None
        self.bonnerep = None


def create_enonce_eleves(chemin_liste, nb_eleves, nb_questions, graine):


    with open(chemin_liste, 'r') as file:
        # Read each line in the file
        compt_quest=0
        compt_task=1
        for line in file:
            match compt_task:
                case 1:
                    None

                case 2 | 3 | 4 | 5:
                    None

                case 6:
                    None

                case 7:
                    None
            
                case 8:
                    None

            # Print each line
            print(line.strip())
        contents = file.read()


#zone de test

create_enonce_eleves('C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_finannee\\QCM_cinema.txt',None,None,None)