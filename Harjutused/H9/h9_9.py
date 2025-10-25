# Loo programm, mis loob suvalised tehted 1-100 arvudega.

import random  # impordib random mooduli

for _ in range(5):  # kordab 5 korda
    tehe = random.choice(["+", "-", "*", "/"])  # valib suvalise tehte
    arv1 = random.randint(1, 100)  # genereerib suvalise arvu 1-100
    arv2 = random.randint(1, 100)  # genereerib suvalise arvu 1-100

    if tehe == "+":  # kui tehe on liitmine
        tulemus = arv1 + arv2  # liidab arvud
    elif tehe == "-":  # kui tehe on lahutamine
        tulemus = arv1 - arv2  # lahutab arvud
    elif tehe == "*":  # kui tehe on korrutamine
        tulemus = arv1 * arv2  # korrutab arvud
    elif tehe == "/":  # kui tehe on jagamine
        while arv2 == 0:  # kontrollib, et jagaja ei oleks null
            arv2 = random.randint(1, 100)  # genereerib uue jagaja
        tulemus = arv1 / arv2  # jagab arvud

    print(f"{arv1} {tehe} {arv2} = {tulemus}")  # prindib tehted ja tulemuse