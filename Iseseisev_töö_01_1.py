# 1. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# 	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# 	eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
# 	kood mis teavitab paaris või paaritust arvust - 1p
# 	kuvatakse programmi pealkiri - 1p
# 	kood kommenteeritud - 1p

print("=== Paaris või Paaritu Kontroll ===")  # programmi pealkiri

try: # laseme kasutajal sisestada int tüüpi numbri ja teeme kontrolli, et see ikka on int tüüpi
    kas_on_paaris = int(input("Palun sisesta nullist erinev täisarvuline number ning programm ütleb, kas see on paarisarv või mitte: "))
except: # kui ei ole int tüüpi, anname veateate
    print("See ei ole ju üldsegi mitte number! Proovi uuesti!")   
else:
    if kas_on_paaris == 0: # teeme kontrolli, et sisestatud number ei oleks 0. kui on 0, anname veateate
        print("Miks sa nulli sisestasid? Proovi uuesti!")
    elif kas_on_paaris % 2 == 0: # kui on paarisarv, kuvame järgmise teate
        print(f"Sinu sisestatud arv {kas_on_paaris} on paarisarv")
    else: # kui on paaritu arv, kuvame järgmise teate
        print(f"Sinu sisestatud arv {kas_on_paaris} ei ole paarisarv")


