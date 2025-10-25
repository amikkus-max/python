# Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75

#     Leia paaris ja paaritud arvud ning lisa oma loendisse
#     Kuva paaris ja paritute arvude summad

loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
paaris_loend = []
paaritu_loend = []
for i in range(len(loend)):
    if loend[i] % 2 == 0:
        paaris_loend.append(loend[i])
    else:
        paaritu_loend.append(loend[i])

print("Paaris loend: ", paaris_loend, "summa: ", sum(paaris_loend))
print("Paaritu loend: ", paaritu_loend, "summa: ", sum(paaritu_loend))