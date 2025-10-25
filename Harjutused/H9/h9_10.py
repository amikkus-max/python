# Täienda eelmist ülesannet ja kasutaja käest küsitakse vastust.

#     Õiged vastused loetakse kokku
#     Kui saab vähemalt poole punktid, siis saab A, muul juhul MA

import random  # impordib random mooduli

correct = 0  # õigete vastuste loendur

for _ in range(5):  # kordab 5 korda
    tehe = random.choice(["+", "-", "*", "/"])  # valib suvalise tehte
    arv1 = random.randint(1, 100)  # genereerib suvalise arvu 1-100
    arv2 = random.randint(1, 100)  # genereerib suvalise arvu 1-100

    if tehe == "+":  # kui tehe on liitmine
        tulemus = arv1 + arv2  # liidab arvud
        vastus = float(input(f"Mis on {arv1} + {arv2}? "))  # küsib kasutajalt vastust
        correct = correct + 1 if vastus == tulemus else correct  # kontrollib vastust
    elif tehe == "-":  # kui tehe on lahutamine
        tulemus = arv1 - arv2  # lahutab arvud
        vastus = float(input(f"Mis on {arv1} - {arv2}? "))  # küsib kasutajalt vastust
        correct = correct + 1 if vastus == tulemus else correct  # kontrollib vastust
    elif tehe == "*":  # kui tehe on korrutamine
        tulemus = arv1 * arv2  # korrutab arvud
        vastus = float(input(f"Mis on {arv1} * {arv2}? "))  # küsib kasutajalt vastust
        correct = correct + 1 if vastus == tulemus else correct  # kontrollib vastust
    elif tehe == "/":  # kui tehe on jagamine
        while arv2 == 0:  # kontrollib, et jagaja ei oleks null
            arv2 = random.randint(1, 100)  # genereerib uue jagaja
        tulemus = arv1 / arv2  # jagab arvud
        vastus = float(input(f"Mis on {arv1} / {arv2}? "))  # küsib kasutajalt vastust
        correct = correct + 1 if vastus == tulemus else correct  # kontrollib vastust

    print(f"Õig vastus: {arv1} {tehe} {arv2} = {tulemus}")  # prindib tehted ja tulemuse
    print(f"Sinu vastus: {vastus}")  # prindib kasutaja vastused

if correct >= 3:  # kui õiged vastused on vähemalt 3
    print("Said hinde A")  # prindib hinde A
else:  # muul juhul
    print("Said hinde MA")  # prindib hinde MA