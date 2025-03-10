import os
import random

class Question :

    """Classe pour question"""

    def __init__ (self) :
        self.enonce = None
        self.reponses = []
        self.bonnerep = None
        self.bonnereptext = None


def create_enonce_eleves(chemin_liste, nb_eleves, nb_questions, graine):


    with open(chemin_liste, 'r') as file:
        # Read each line in the file
        ListeQuestions = []
        
        compt_quest = 0
        compt_task = 1
        temp_enonce = None
        temp_reponses=[]
        temp_bonnerep = None
        temp_bonnereptext = None

        for line in file:
            if compt_quest < nb_questions :
                match compt_task:
                    case 1:
                        temp_enonce = line.strip()
                        compt_task += 1

                        print("DEBUG - Enoncé lu :", temp_enonce)


                    case 2 | 3 | 4 | 5:
                        temp_reponses.append(line.strip())
                        compt_task += 1
                        print("DEBUG - Réponses lue :", temp_reponses)

                    case 6:
                        temp_bonnerep = int(line.strip())
                        temp_bonnereptext = temp_reponses[temp_bonnerep-1]
                        compt_task += 1
                        print("DEBUG - Bonne réponse lue :", temp_bonnerep, "-", temp_bonnereptext)

                    case 7:
                        None
                        
                        TempQuestion = Question()
                        TempQuestion.enonce = temp_enonce
                        TempQuestion.reponses = temp_reponses
                        TempQuestion.bonnerep = temp_bonnerep
                        TempQuestion.bonnereptext = temp_bonnereptext

                        ListeQuestions.append(TempQuestion)

                        temp_enonce = None
                        temp_reponses=[]
                        temp_bonnerep = None
                        temp_bonnereptext = None

                        compt_task = 1
                        compt_quest += 1

                        print("DEBUG - Liste Progrès :", ListeQuestions)

            # Print each line
            print(line.strip())
        contents = file.read()



#zone de test

create_enonce_eleves('C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_finannee\\QCM_cinema.txt',None,10,None)