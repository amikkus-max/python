# 2. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR.
# 	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# 	kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
# 	küsitakse valuuta kogust ja tehakse arvutused - 2p
# 	kood kommenteeritud - 1p


kurss = 15.6466  # määrame euro ja krooni vahetuskursi

print("=== Eurokalkulaator ===")  # programmi pealkiri
print("Tere tulemast Eurokalkulaatorisse! Siin saad konvertida EUR->EEK või EEK->EUR") 
print("Programm kasutab vahetuskurssi 1 EUR = 15.6466 EEK") 
print("Vali, kumba soovid teha:") 
print("1: EUR -> EEK") 
print("2: EEK -> EUR") 
valik = input("Sisesta 1 või 2: ") # küsime kasutajalt valikut
if valik != "1" and valik != "2":  # kui kasutaja valik ei ole 1 ega 2, anname veateate
    print("Nii ei saa! Palun vali 1 või 2!")
else:  # kui valik on korrektne, jätkame
    try:  # proovime kasutajalt küsida valuuta kogust
        kogus = float(input("Sisesta summa, mida soovid konvertida: ")) # küsime kasutajalt konvertitavat summat
    except:  # kui kasutaja ei sisesta float tüüpi numbrit (mis valuuta peaks olema), anname veateate
        print("Valuuta kogus peab olema number!")
    else:  # kui kasutaja sisestas korrektse valuuta koguse, teeme arvutused
        if valik == "1":  # kui valik on 1, konvertime EUR -> EEK
            tulemus = kogus * kurss  # arvutame tulemuse
            print(f"{kogus} EUR on {tulemus:.2f} EEK")  # kuvame tulemuse, ümardame kahe komakohani
        else:  # kui valik on 2, konvertime EEK -> EUR
            tulemus = kogus / kurss  # arvutame tulemuse
            print(f"{kogus} EEK on {tulemus:.2f} EUR")  # kuvame tulemuse, ümardame kahe komakohani
