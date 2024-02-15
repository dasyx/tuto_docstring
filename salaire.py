def lire_entrees():
    while True :
        salaire_mensuel = float(input(f"Saisissez votre salaire mensuel : "))
        if salaire_mensuel < 0 :
            print("Votre salaire doit être un nombre positif")
            continue
        else :
            print(f"Le salaire saisi est de {salaire_mensuel} euros.")
            return salaire_mensuel
        
    """  heures_semaine = float(input(f'Saisissez vos heures travaillées par semaine : {heures} ')) """

lire_entrees()