# 6. Salakeel
# 	sinu programm küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida - 1p
# 	kasutaja sisestab tavalise sõna, mis muudetakse salakeeleks - 1p
# 	kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks - 1p
# 	kood kommenteeritud - 1p

tahestik =     ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','Š','š','Z','z','Ž','ž','T','t','U','u','V','v','W','w','Õ','õ','Ä','ä','Ö','ö','Ü','ü','X','x','Y','y','0','1','2','3','4','5','6','7','8','9']
uus_tahestik = ['P','y','E','0','j','G','š','p','O','q','2','a','u','4','n','6','e','F','o','v','ž','Ž','X','Y','L','T','z','D','x','H','i','Q','N','8','B','C','Z','R','w','U','ö','s','7','M','5','m','Ö','J','d','l','I','Ü','g','1','9','b','r','ä','3','W','k','Ä','f','c','Š','Õ','õ','V','ü','A','h','t','S','K']

# import random
# uus_tahestik = random.sample(tahestik, k=len(tahestik))

# Programmi pealkiri ning tutvustus
print("""=== Salakeel ===
    Antud programmi abil saad oma sõnumeid salakeelde tõlkida ja tagasi tavakeelde.
    Valik 1: Tavaline tekst -> Salakeel
    Valik 2: Salakeel -> Tavaline tekst
    Kõigepealt sisesta oma sõnum ning seejärel vali, kumba soovid teha:""")

sonum = input("Sisesta sõnum: ")
valik = input("Kas soovid oma sõnumit salakeelde tõlkida (1) või tavakeelde tagasi tõlkida (2)? ")

# kui valik on 1, siis tõlgime tavakeelest salakeelde
# käime tähthaaval läbi kasutaja sisestatud sõnumi, kui täht on listis "tahestik", siis leiame selle indeksi ja võtame listist "uus_tahestik" sama indeksi tähe ja lisame selle uude sõnumisse
# kui täht ei ole meie listis "tahestik" (nt tühik, koma, punkt vms), siis lisame sellesama tähe lihtsalt uude sõnumisse
# kui valik on 2, siis teeme sama, aga vastupidi - käime läbi listi "uus_tahestik" ja leiame tähe indeksi ning võtame listist "tahestik" sama indeksi tähe ja lisame selle uude sõnumisse
# kui valik ei ole 1 ega 2, anname veateate

if valik == "1":
    salakeel = ""
    for i in sonum:
        if i in tahestik:
            salakeel += uus_tahestik[tahestik.index(i)]
        else:
            salakeel += i
    print(f"Sinu sõnum \"{sonum}\" on salakeeles: \"{salakeel}\"")
elif valik == "2":
    tavakeel = ""
    for i in sonum:
        if i in uus_tahestik:
            tavakeel += tahestik[uus_tahestik.index(i)]
        else:
            tavakeel += i
    print(f"Sinu sõnum \"{sonum}\" on tavakeeles: \"{tavakeel}\"")
else:
    print("Nii ei saa! Palun vali 1 või 2!")


