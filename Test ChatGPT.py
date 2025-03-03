import os

def lire_questions(fichier):
    """Lit les questions et réponses depuis un fichier."""
    questions = []
    if not os.path.exists(fichier):
        print(f"Erreur : Le fichier {fichier} n'existe pas.")
        return questions
    
    with open(fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            try:
                question, options, reponse = ligne.strip().split("|")
                options = options.split(",")
                reponse = int(reponse)  # Convertir la réponse en entier
                if 1 <= reponse <= len(options):  # Vérifier que la réponse est valide
                    questions.append((question, options, reponse))
                else:
                    print(f"⚠ Problème dans la ligne : {ligne.strip()}")
            except ValueError:
                print(f"⚠ Erreur de format dans la ligne : {ligne.strip()}")
    
    return questions

def poser_question(question, options, reponse_correcte):
    """Pose une question et vérifie la réponse."""
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            reponse_utilisateur = int(input("Votre réponse (1-4) : "))
            if 1 <= reponse_utilisateur <= len(options):
                if reponse_utilisateur == reponse_correcte:
                    print("✅ Bonne réponse !")
                    return 1
                else:
                    print(f"❌ Mauvaise réponse. La bonne réponse était : {options[reponse_correcte - 1]}")
                    return 0
            else:
                print("⚠ Choix invalide, veuillez entrer un nombre entre 1 et", len(options))
        except ValueError:
            print("⚠ Entrée invalide, veuillez entrer un nombre.")

# Programme principal
fichier_questions = "C:\\Users\Aziz\\Documents\\Repositories\\Projet fin d'année QCM\\Projet-fin-d-ann-e-QCM-\\questions.txt"
questions = lire_questions(fichier_questions)

if not questions:
    print("Erreur : Aucune question valide trouvée dans le fichier.")
else:
    score = 0
    for question, options, reponse in questions:
        score += poser_question(question, options, reponse)

    print(f"\nVotre score final : {score} / {len(questions)}")
