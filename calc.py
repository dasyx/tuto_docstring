nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le second nombre : "))
operation = input("Entrez l'opération à effectuer (+, -, *, /) : ")

def check_operation(operation):
    match operation:
        case "+":
            total = nombre1 + nombre2
            print(f"Le résultat de l'addition est : {total}")
        case "-":
            total = nombre1 - nombre2
            print(f"Le résultat de la soustraction est : {total}")
        case "*":
            total = nombre1 * nombre2
            print(f"Le résultat de la multiplication est : {total}")
        case "/":
            if nombre2 == 0:
                print("La division par 0 n'est pas autorisée")
            else :
                total = nombre1 / nombre2
                print(f"Le résultat de la division est : {total}")
        case _:
            print("Veuillez saisir une opération valide")

check_operation(operation)