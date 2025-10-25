# Programm peaks kasutajalt küsima toote nime, mida ta soovib osta
# Seejärel küsitakse kasutajalt soovitud kogust
# Kontrolli, kas otsitav toode on sõnastikus olemas:
# Kui toodet ei ole, kuvatakse sõnum, et toodet ei leitud
# Kontrolli, kas soovitud kogus on saadaval
# Kui kogus on saadaval, arvutatakse ja kuvatakse ostu kogusumma
# Kui kogus ei ole piisav, teavitatakse kasutajat sellest
# Kui ost on võimalik, vähendatakse toote kogust laoseisus vastavalt ostetud kogusele
# Lõpetuseks kuvatakse uuendatud laoseisu info.

tooted = {
    'piim': {'kogus': 20, 'hind': 1.19},
    'küpsised': {'kogus': 20, 'hind': 4.99},
    'või': {'kogus': 20, 'hind': 2.29},
    'juust': {'kogus': 15, 'hind': 1.9},
    'leib': {'kogus': 15, 'hind': 2.59},
    'jogurt': {'kogus': 18, 'hind': 3.65},
    'õunad': {'kogus': 35, 'hind': 3.15},
    'apelsinid': {'kogus': 40, 'hind': 0.99},
    'banaanid': {'kogus': 23, 'hind': 1.29}
}

try:
    toode = input("lisa toode: ").lower()
    kogus = int(input("vali kogus: "))

    if toode in tooted.keys():
        if kogus <= tooted[toode]["kogus"] and kogus > 0:
            print("===ARVE===")
            summa= kogus * tooted[toode]["hind"]
            print(f"{summa:.2f} €")

            tooted[toode]["kogus"] -= kogus  # võtab koguse maha, (süvene kodus - märgi kasutamisele siin näites)
            print(tooted)

        else:
            print("Pole piisavalt")
    else:
        print(f"Toodet" "{toode}" " hetkel ole")
except:
    print("Midagi sisestasid valesti")