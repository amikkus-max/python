# Sulle on saadetud õpilaste keskmised hinded, mille lisasid loendisse. 
# Eralda hinded ning leia kogu rühma parim ja kehvem tulemus ning keskmine hinne.
# ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]

ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]

ryhma_hinded_sonastik = {}  # tühi sõnastik
for i in range(len(ryhma_hinded)):  # läbib hinded
    nimi, hinne = ryhma_hinded[i].split()  # jagab nime ja hinde
    ryhma_hinded_sonastik[nimi] = float(hinne)  # lisab sõnastikku

print("Kõrgeim hinne: ", max(ryhma_hinded_sonastik.values()))  # kõrgeim hinne
print("Madalaim hinne: ", min(ryhma_hinded_sonastik.values()))  # madalaim hinne
print("Keskmine hinne: ", sum(ryhma_hinded_sonastik.values()) / len(ryhma_hinded_sonastik))  # keskmine hinne
print(ryhma_hinded_sonastik)  # prindib sõnastiku