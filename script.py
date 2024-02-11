""" super_heros = ["Superman", "Batman", "Wonderwoman", "Aquaman"]

for heros in super_heros:
    print(heros) """

""" for i in range(10):
    print(f"Le nombre actuel est : {i}") """

x = 0
while x < 20:
    x += 1
    if x == 10:
        answer = input("Voulez-vous continuer ? (oui ou non) : ")
        if answer == "oui":
            x = 10
        else:
            break
    print(x)