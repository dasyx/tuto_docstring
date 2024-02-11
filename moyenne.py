

def check_number():
    numbers = []
    ask_number = input("Veuillez saisir un nouveau nombre (pour terminer la saisie, tapez 'fin') : ")
    while ask_number != "fin":
        ask_number = input("Veuillez saisir un nouveau nombre (pour terminer la saisie, tapez 'fin') : ")
        if ask_number == "fin":
            break
check_number()