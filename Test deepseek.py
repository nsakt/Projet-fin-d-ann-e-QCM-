import random

def lire_fichier_questions(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        lignes = fichier.readlines()
    
    questions = []
    i = 0
    while i < len(lignes):
        if lignes[i].strip() == '':
            i += 1
            continue
        
        question = lignes[i].strip()
        reponses = [lignes[i+j+1].strip() for j in range(4)]
        bonne_reponse = int(lignes[i+5].strip())
        questions.append({
            'question': question,
            'reponses': reponses,
            'bonne_reponse': bonne_reponse
        })
        i += 7  # Passer à la prochaine question
    
    return questions

def generer_sujets(questions, nb_eleves, nb_questions_par_eleve, graine):
    random.seed(graine)
    sujets = []
    correction = []
    
    for eleve in range(1, nb_eleves + 1):
        questions_eleve = random.sample(questions, nb_questions_par_eleve)
        sujet = []
        corrige = []
        
        for q in questions_eleve:
            reponses = q['reponses'].copy()
            bonne_reponse = reponses[q['bonne_reponse'] - 1]
            random.shuffle(reponses)
            nouvelle_bonne_reponse = reponses.index(bonne_reponse) + 1
            
            sujet.append({
                'question': q['question'],
                'reponses': reponses
            })
            corrige.append({
                'question': q['question'],
                'bonne_reponse': nouvelle_bonne_reponse
            })
        
        sujets.append(sujet)
        correction.append(corrige)
    
    return sujets, correction

def ecrire_sujets(sujets, prefixe_fichier):
    for i, sujet in enumerate(sujets):
        with open(f"{prefixe_fichier}_eleve_{i+1}.txt", 'w', encoding='utf-8') as fichier:
            for j, q in enumerate(sujet):
                fichier.write(f"Question {j+1}:\n")
                fichier.write(f"{q['question']}\n")
                for k, reponse in enumerate(q['reponses']):
                    fichier.write(f"{k+1}. {reponse}\n")
                fichier.write("\n")

def ecrire_correction(correction, nom_fichier):
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        for i, corrige in enumerate(correction):
            fichier.write(f"Sujet {i+1}:\n")
            for j, q in enumerate(corrige):
                fichier.write(f"Question {j+1}: {q['bonne_reponse']}\n")
            fichier.write("\n")

def main():
    nom_fichier_questions = input("Entrez le nom du fichier contenant les questions: ")
    nb_eleves = int(input("Entrez le nombre d'élèves: "))
    nb_questions_par_eleve = int(input("Entrez le nombre de questions par élève (5, 10, 15 ou 20): "))
    graine = int(input("Entrez la graine pour la génération aléatoire: "))
    
    questions = lire_fichier_questions(nom_fichier_questions)
    sujets, correction = generer_sujets(questions, nb_eleves, nb_questions_par_eleve, graine)
    
    ecrire_sujets(sujets, "sujet")
    ecrire_correction(correction, "correction.txt")
    
    print("Les sujets et le fichier de correction ont été générés avec succès.")

if __name__ == "__main__":
    main()