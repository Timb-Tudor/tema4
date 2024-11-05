import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

incercari_ramase = 6
litere_incercate = []

gasit = False

print(" ".join(progres))

while not gasit and incercari_ramase > 0:
    litera = input("Introdu o litera: ")

    if len(litera) != 1 or not litera.isalpha():
        print("Introdu o litera valida: ")

    litere_incercate.append(litera)
    print(f"Litere incercate: {litere_incercate}")

    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera

        print("Ai ghicit o litera!")
    else:
        incercari_ramase -= 1
        print(f"Incercari ramase: {incercari_ramase}")

    print("Progres: " + " ".join(progres))

if "_" not in progres:
    print(f"Felicitari! Ai ghicit cuvantul: {cuvant_de_ghicit}")
else:
    print(f"Ai pierdut! Cuvantul era: {cuvant_de_ghicit}")

