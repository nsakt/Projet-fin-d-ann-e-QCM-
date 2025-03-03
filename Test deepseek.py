def lire_fichier_questions(nom_fichier):
    """
    Lit le fichier texte contenant les questions et les réponses.
    Retourne une liste de dictionnaires, chaque dictionnaire représentant une question.
    """
    questions = []
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            lignes = fichier.readlines()
    except FileNotFoundError:
        print(f"Erreur: Le fichier '{nom_fichier}' n'a pas été trouvé.")
        return questions

    i = 0
    while i < len(lignes):
        # Ignorer les lignes vides
        if lignes[i].strip() == '':
            i += 1
            continue

        # Lire la question
        question = lignes[i].strip()
        i += 1

        # Lire les 4 réponses
        reponses = [lignes[i + j].strip() for j in range(4)]
        i += 4

        # Lire le numéro de la bonne réponse
        bonne_reponse = int(lignes[i].strip())
        i += 1

        # Ajouter la question à la liste
        questions.append({
            'question': question,
            'reponses': reponses,
            'bonne_reponse': bonne_reponse
        })

    return questions

def afficher_question(question):
    """
    Affiche une question et ses réponses.
    """
    print(question['question'])
    for idx, reponse in enumerate(question['reponses']):
        print(f"{idx + 1}. {reponse}")

def demander_reponse():
    """
    Demande à l'utilisateur de saisir sa réponse.
    Retourne un entier correspondant au numéro de la réponse choisie.
    """
    while True:
        try:
            choix = int(input("Votre réponse (1-4) : "))
            if 1 <= choix <= 4:
                return choix
            else:
                print("Veuillez entrer un nombre entre 1 et 4.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def jouer_qcm(questions):
    """
    Joue le QCM en affichant chaque question et en vérifiant les réponses.
    """
    score = 0
    for idx, question in enumerate(questions):
        print(f"\nQuestion {idx + 1}:")
        afficher_question(question)
        choix_utilisateur = demander_reponse()
        if choix_utilisateur == question['bonne_reponse']:
            print("Bonne réponse !")
            score += 1
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {question['bonne_reponse']}")

    print(f"\nVotre score final est de {score}/{len(questions)}")

def main():
    """
    Fonction principale du programme.
    """
    nom_fichier = input("Entrez le nom du fichier contenant les questions : ")
    questions = lire_fichier_questions(nom_fichier)

    if not questions:
        print("Aucune question n'a été chargée. Vérifiez le fichier.")
        return

    print("\nBienvenue au QCM !")
    jouer_qcm(questions)

if __name__ == "__main__":
    main()