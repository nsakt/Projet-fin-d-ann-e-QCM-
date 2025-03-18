import os
import random
from docx.shared import Pt
from docx import Document
from docx.enum.text import WD_BREAK
from docx.enum.text import WD_ALIGN_PARAGRAPH



class Question :

    """Classe pour question"""

    def __init__ (self) :
        self.enonce = None
        self.reponses = []
        self.bonnerep = None
        self.bonnereptext = None

    def __len__(self):
        return len(self.reponses)
    


def create_enonce_eleve(chemin_liste, nb_questions):
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
                        
    return ListeQuestions

def shuffle_enonce_eleves(ListeBase):
    """Mélange l'énoncé d'un élève (une liste de questions) induviduels tout en gardant trace de la bonne réponse"""
    random.shuffle(ListeBase)
    for elt in ListeBase:
        random.shuffle(elt.reponses)
        for i in range(4):
            if elt.reponses[i] == elt.bonnereptext:
                elt.bonnerep = i+1
    return ListeBase


def create_enonce_eleves(chemin_liste, nb_questions, nb_eleve):
    """Crée une liste d'énoncés mélangés pour un nombre donné d'élèves, utilisant les fonctions précédentes"""
    Enonce_Final = []
    Liste_Questions_Temp = []
    for i in range(nb_eleve):
        Liste_Questions_Temp = create_enonce_eleve(chemin_liste,nb_questions)
        Liste_Questions_Temp = shuffle_enonce_eleves(Liste_Questions_Temp)
        Enonce_Final.append(Liste_Questions_Temp)
    return Enonce_Final


def create_correction_enonce(Enonce_Base):  
    """Crée une liste de set de réponses pour les énoncés donnés, sous forme de ints"""
    liste_rep_enonce=[]
    subliste_rep=[]
    for elt in Enonce_Base:
        for i in range(len(elt)):
            subliste_rep.append(elt[i].bonnerep)
        liste_rep_enonce.append(subliste_rep)
        subliste_rep=[]
    print(liste_rep_enonce)
    return liste_rep_enonce


def create_doc_sujets(enonce_total,nom_document):
    doc_sujet = Document()
    


    tempstring = ''
    cmpt_sujets=1
    for elt in enonce_total:
        doc_sujet.add_paragraph('Nom et Prenom : ')
        doc_sujet.add_paragraph('Sujet ' + str(cmpt_sujets))
        for i in range(len(elt)):
            paragraph = doc_sujet.add_paragraph('Question : ' + str(i+1))
            doc_sujet.add_paragraph(elt[i].enonce)

           
            paragraph_format = paragraph.paragraph_format
            paragraph_format.space_before, paragraph_format.space_after
            (None, None)  # inherited by default

            paragraph_format.space_before = Pt(3)
            paragraph_format.space_before.pt
            3

            paragraph_format.space_after = Pt(3)
            paragraph_format.space_after.pt
            3
            tempstring += ' | '
            
            for f in range(4):
                match f:
                    case 0 :
                        tempstring += 'a -'
                    
                    case 1 :
                        tempstring += 'b -'

                    case 2 :
                        tempstring += 'c -'

                    case 3 :
                        tempstring += 'd -'

                tempstring += str(elt[i].reponses[f]) + ' | '

            paragraph = doc_sujet.add_paragraph(tempstring)
            tempstring = ''
        cmpt_sujets +=1
        doc_sujet.add_page_break()
    

    doc_sujet.save('C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_finannee\\'+nom_document+'.docx')



def create_doc_correction(liste_corrections,nom_document):
    
    
    doc_corrige = Document()
    tempstring = ''
    cmpt_sujets=1
    cmpt_space=1
    for elt in liste_corrections :
        doc_corrige.add_paragraph('Sujet ' + str(cmpt_sujets))
        for i in range(len(elt)):
            match elt[i]:
                case 1:
                    tempstring += 'a'

                case 2:
                    tempstring += 'b'
                
                case 3:
                    tempstring += 'c'
                
                case 4:
                    tempstring += 'd'
            if cmpt_space == 5:
                tempstring += ' '
                cmpt_space = 1
            else:
                cmpt_space += 1
        
        cmpt_sujets += 1
        doc_corrige.add_paragraph(tempstring)
        tempstring = ''
        doc_corrige.add_paragraph(tempstring)
                
    doc_corrige.add_paragraph(tempstring)
    doc_corrige.save('C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_finannee\\'+nom_document+'.docx')






def create_doc_sujets_run(enonce_total,nom_document):
    

    tempstring = ''
    cmpt_sujets=1

    for elt in enonce_total:
        doc_sujet = Document()
        run = doc_sujet.add_paragraph().add_run()
        font = run.font
        font.name = 'Calibri'
        font.size = Pt(9)
        run.add_text('Nom et Prenom : ')
        run.add_break()
        run.add_text('Sujet  ' + str(cmpt_sujets))
        run.add_break()
        for i in range(len(elt)):
            run.add_text('Question : ' + str(i+1))
            run.add_break()
            run.add_text(elt[i].enonce)
            run.add_break()

            tempstring += ' | '
            
            for f in range(4):
                match f:
                    case 0 :
                        tempstring += 'a -'
                    
                    case 1 :
                        tempstring += 'b -'

                    case 2 :
                        tempstring += 'c -'

                    case 3 :
                        tempstring += 'd -'

                tempstring += str(elt[i].reponses[f]) + ' | '

            run.add_text(tempstring)
            run.add_break()
            run.add_break()
            tempstring = ''
        doc_sujet.save('C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_finannee\\' + nom_document + 'sujet' + str(cmpt_sujets) +'.docx')
        cmpt_sujets +=1
        

    

    doc_sujet.save('C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_finannee\\'+nom_document+'.docx')



#zone de test

Enonce_test = create_enonce_eleves('C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_finannee\\QCM_cinema.txt',20,5)
print(Enonce_test)

for elt in Enonce_test:
    print("----------------------")
    for i in range(5):
        print (elt[i].enonce)

create_doc_sujets_run(Enonce_test,"TestEnonce")

Correction_Test = create_correction_enonce(Enonce_test)

create_doc_correction(Correction_Test,"TestCorrection")


document = Document()
run = document.add_paragraph().add_run()
font = run.font
font.name = 'Calibri'
font.size = Pt(100)
run.add_text('SUCK IT')
document.save('C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_finannee\\tester.docx')