import os
import random

class Question :

    """Classe pour question"""

    def __init__ (self) :
        self.enonce = None
        self.reponses = []
        self.bonnerep = None
        self.bonnereptext = None

    def __len__(self):
        return len(self.reponses)


def create_enonce_eleves(chemin_liste, nb_eleves, nb_questions):
    """Création d'une liste de questions a partir d'un fichier texte formaté comme décrit dans l'exercice, selon un nombre d'élèves"""

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

                        print("DEBUG - Question Enrgistrée - Enoncé :", ListeQuestions[compt_quest].enonce, " - Reponses: ", ListeQuestions[compt_quest].reponses, " - Bonne réponse : ", ListeQuestions[compt_quest].bonnerep, " ", ListeQuestions[compt_quest].bonnereptext)

                        compt_task = 1
                        compt_quest += 1

                        print("DEBUG - Liste total :", ListeQuestions)
                        


            # Print each line
            '''print(line.strip())
        contents = file.read()'''
    return ListeQuestions


def shuffle_enonce_eleves(ListeBase):
    random.shuffle(ListeBase)
    for elt in ListeBase:
        random.shuffle(elt.reponses)
        for i in range(4):
            if elt.reponses[i] == elt.bonnereptext:
                elt.bonnerep = i+1











#zone de test

Enonce_test = create_enonce_eleves('C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_finannee\\QCM_cinema.txt',10,10)
print(Enonce_test)

shuffle_enonce_eleves(Enonce_test)