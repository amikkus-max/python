# Harjutus 7


# Kasuta etteantud loendit ja toesta nõutud operatsioonid. Lisa igale tegevusele kommentaar ja vasta täislausega:
# "jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3
# Kuva mõõdetava kuu nimetus
# Kuva viimase mõõtmise tulemus
# Kuva ainult temperatuurid
# Leia kuu maksimaalne ja minimaalne temperatuur
# Leia kuu keskmine temperatuur
# Mitu korda esines -20 kraadi
# Eemalda element nr 5
# Lisa 5. elemendi kohale temperatuur, mis on sinu vanus
# Sorteeri temperatuurid nimekirjas kasvavas järjekorras

m66tmised = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]
print(f"mõõdetav kuu: {m66tmised[0]}")
print(f"viimase kuu tulemus: {m66tmised[-1]}")
print(f"Mõõtmised: {m66tmised[1:]}")
m66tmised.pop(0) #eemaldab kirje asukohast ()
print(f"min: {min(m66tmised)} max: {max(m66tmised)}")
print(f"Keskmine temp: {round(sum(m66tmised)/len(m66tmised),2)}")
print(f"-20 kraadi esineb {m66tmised.count(-20)} korda")
m66tmised.pop(4)
m66tmised.insert(4,40)
m66tmised.sort()
print(m66tmised)













# Loo lugudest loend (koos numbrite ja jutumärkidega)

# Kuva kasutajale kõik lood massiivist
# Küsi millist lugu ta "kuulata" soovib
# Kuva kasutaja valitud lugu

# nimede_loend = ["Alice", "Bob", "Carol", "Dave", "Eve"]
# 
# nimede_loend.append("Jyri")
# nimede_loend.insert(2,"Mari")
# nimede_loend.remove("Bob")
# 
# print(nimede_loend[2:4])
# 
# for i in nimede_loend:
# #    if i == "Carol":
# #        break
#     print(i)
    
albumid = ['1. ALIKA – "Bridges"','2. Anett x Fredi – "Read Between The Lines"','3. villemdrillem – "leekiv armastus"','4. Clicherik & Mäx – "PAKSUD"','5. nublu – "ära ärata"','6. NOËP – "Move Your Feet"','7. Trad.Attack! – "Bring It On"','8. Bedwetters – "It Is What It Is"','9. Reket – "Panama paberid"','10. Grete Paia – "Võluväel"']
print(20*"-","KÕIK LOOD",20*"-")
for i in albumid:
    print(i)
    
lugu = int(input("Millist lugu: "))
print(f"Mängin: {albumid[lugu-1]}")



