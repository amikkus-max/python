# 1.2. Aasta liblikas
# Koostada programm, mille
# 1. real luuakse muutuja nimega aasta ning antakse sellele väärtuseks 2020 (arvuna);
# 2. real luuakse muutuja nimega liblikas ning antakse sellele väärtuseks "teelehe-mosaiikliblikas" (sõnena);
# 3. real luuakse muutuja nimega lause_keskosa ning antakse sellele väärtuseks ". aasta liblikas on " (sõnena);
# 4. real luuakse muutuja nimega lause, mille väärtuse saamiseks ühendatakse üheks sõnaks muutujad aasta, lause_keskosa ja liblikas 
# (vajadusel tuleb kasutada funktsiooni, mis teisendab arvu sõneks);
# 5. real väljastatakse muutuja lause väärtus ekraanile.


aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta) + lause_keskosa + liblikas
print(lause)
