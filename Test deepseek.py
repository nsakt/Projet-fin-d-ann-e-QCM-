# Définition des questions du QCM
questions = {
    "Quel est le langage utilisé pour le développement web côté client ?": {
        "options": ["1. Python", "2. JavaScript", "3. Java", "4. C++"],
        "réponse": 2
    },
    "Quelle est la capitale de la France ?": {
        "options": ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
        "réponse": 3
    },
    "Combien font 5 * 6 ?": {
        "options": ["1. 30", "2. 25", "3. 35", "4. 40"],
        "réponse": 1
    }
}

# Initialisation du score
score = 0

# Parcours des questions
for question, data in questions.items():
    print("\n" + question)
    for option in data["options"]:
        print(option)
    
    # Récupération de la réponse utilisateur
    try:
        réponse_utilisateur = int(input("Votre réponse (1-4) : "))
        if réponse_utilisateur == data["réponse"]:
            print("✅ Bonne réponse !")
            score += 1
        else:
            print("❌ Mauvaise réponse.")
    except ValueError:
        print("⚠️ Entrée invalide, réponse ignorée.")

# Affichage du score final
print(f"\nVotre score final : {score} / {len(questions)}")
