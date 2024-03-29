def lire_salaire_mensuel():
    while True:
        try:
            salaire_mensuel = float(input("Saisissez votre salaire mensuel (en euros) : "))
            if salaire_mensuel < 0:
                print("Votre salaire doit être un nombre positif.")
            else:
                return salaire_mensuel
        except ValueError:
            print("Veuillez saisir un nombre valide.")

def lire_heures_semaine():
    while True:
        try:
            heures_semaine = float(input("Saisissez vos heures travaillées par semaine : "))
            if heures_semaine < 0:
                print("Votre nombre d'heures travaillées doit être un nombre positif.")
            else:
                return heures_semaine
        except ValueError:
            print("Veuillez saisir un nombre valide.")

def calculer_salaire_horaire(salaire_mensuel, heures_semaine):
    salaire_horaire = salaire_mensuel / (heures_semaine * 4.33)
    return salaire_horaire

def lire_entrees():
    salaire_mensuel = lire_salaire_mensuel()
    heures_semaine = lire_heures_semaine()
    salaire_horaire = calculer_salaire_horaire(salaire_mensuel, heures_semaine)
    print(f"Le salaire saisi est de {salaire_mensuel} euros.")
    print(f"Le nombre d'heures travaillées est de {heures_semaine} heures.")
    print(f"Le salaire horaire est de : {round(salaire_horaire, 2)} euros")

lire_entrees()

