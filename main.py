import os
import random

class Question :

    """Classe pour question"""

    def __init__ (self) :
        self.enonce = None
        self.reponses = []
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
                    compt_task =+ 1


                case 2 | 3 | 4 | 5:
                    None
                    compt_task =+ 1

                case 6:
                    None
                    compt_task =+ 1

                case 7:
                    None
                    compt_task =+ 1
            
                case 8:
                    compt_task = 1

            # Print each line
            print(line.strip())
        contents = file.read()


#zone de test

create_enonce_eleves('C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_finannee\\QCM_cinema.txt',None,None,None)