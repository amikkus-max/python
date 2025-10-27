# 1.4. Bussid
# Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega. Eeldame, et reisijaid on vähemalt üks. 
# Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi kohtade arvu (just sellises järjekorras) ning väljastab ekraanile, 
# mitu bussi on vaja ja mitu inimest on viimases bussis (eeldusel, et kõik eelnevad bussid on täis).


reisijad = int(input("Sisesta reisijate arv: "))
bussis_kohad = int(input("Mitu kohta on bussis: "))

busside_arv = reisijad // bussis_kohad + (reisijad % bussis_kohad > 0)
viimases_bussis = reisijad % bussis_kohad
if viimases_bussis == 0:
    print(f"Viimases bussis on {int(reisijad/busside_arv)} reisijat")
else:
    print(f"Viimases bussis on {viimases_bussis} reisijat")

