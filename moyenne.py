def check_number():
    numbers = []
    total_sum = 0
    while True:
        ask_number = input("Veuillez saisir un nouveau nombre entier (pour terminer la saisie, tapez 'fin') : ")
        if ask_number == "fin":
            # boucle sur les résultats de la liste pour afficher une moyenne
            for number in numbers:
                total_sum += number
                average = float(total_sum / len(numbers))
            print(f"La moyenne des nombres saisis est de : {average}")
            break
        try:
            num = int(ask_number)
            numbers.append(num)
            print(numbers)
        except:
            # Si une ValueError est levée, informez l'utilisateur et continuez la boucle
            print("Ce n'est pas un nombre entier valide. Veuillez réessayer.")
            continue  # Passez à la prochaine itération de la boucle

        # Calcul de la moyenne en dehors de la boucle while
        """ if numbers:  # Vérifier que la liste n'est pas vide
            total_sum = sum(numbers)  # Utilisez la fonction sum() pour la somme
            average = total_sum / len(numbers)
            print(f"La moyenne des nombres saisis est de : {average}") """
check_number()
