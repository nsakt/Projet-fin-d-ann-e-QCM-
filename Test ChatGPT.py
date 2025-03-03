def lire_questions(fichier):
    """Lit les questions et réponses depuis un fichier."""
    questions = []
    with open(fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            question, options, reponse = ligne.strip().split("|")
            options = options.split(",")
            questions.append((question, options, int(reponse)))
    return questions

def poser_question(question, options, reponse_correcte):
    """Pose une question et vérifie la réponse."""
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    try:
        reponse_utilisateur = int(input("Votre réponse (1-4) : "))
        if reponse_utilisateur == reponse_correcte:
            print("✅ Bonne réponse !")
            return 1
        else:
            print(f"❌ Mauvaise réponse. La bonne réponse était : {options[reponse_correcte - 1]}")
            return 0
    except ValueError:
        print("⚠️ Entrée invalide, réponse ignorée.")
        return 0

# Programme principal
fichier_questions = "questions.txt"
questions = lire_questions(fichier_questions)
score = 0

for question, options, reponse in questions:
    score += poser_question(question, options, reponse)

print(f"\nVotre score final : {score} / {len(questions)}")
