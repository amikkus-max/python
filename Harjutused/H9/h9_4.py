# Kuva arvud 1-42

#     Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
#     Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
#     Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)

for i in range(1,42):
    if   i%15 == 0:
        print(i, "TIKTAK")
    elif i%5 == 0:
        print(i, "TAK")
    elif i%3 == 0:
        print(i, "TIK")
    else:
        print(i, end=" ")