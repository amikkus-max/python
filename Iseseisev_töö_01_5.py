# 5. Kaugushüpe
# 	kasutaja sisestab 3 kaugushüppe tulemust - 1p
# 	sinu programm leiab ning väljastab parima ja keskmise tulemuse - 2p
# 	programmi dialoog kasutajaga on arusaadav ja üheselt mõistetav - 1p
# 	kood kommenteeritud - 1p

print("=== Kaugushüppe Tulemused ===")  # programmi pealkiri
print("Tere tulemast kaugushüppe tulemuste programmi! Siin saad sisestada oma kolme hüppe tulemuse ning programm leiab parima ja keskmise tulemuse.")
print("Palun sisesta oma hüppe tulemused meetrites (nt 5.67). Ebaõnnestunud katse puhul sisesta 0.")

tulemused = []  # loome tühja listi tulemuste salvestamiseks
while len(tulemused) < 3:  # kordame seni, kuni meil on 3 kehtivat tulemust
    try:
        tulemus = float(input(f"Sisesta hüppe tulemus {len(tulemused) + 1} (meetrites): "))  # küsime kasutajalt hüppe tulemuse
        if tulemus < 0:  # kontrollime, et tulemus ei oleks negatiivne
            print("Hüppe tulemus ei saa olla negatiivne! Proovi uuesti.")
        else:
            tulemused.append(tulemus)  # lisame kehtiva tulemuse listi
    except ValueError:  # kui kasutaja ei sisesta float tüüpi numbrit, anname veateate
        print("Hüppe tulemus peab olema number! Proovi uuesti.")

parim_tulemus = max(tulemused)  # leiame parima tulemuse
keskmine_tulemus = sum(tulemused) / len(tulemused)  # arvutame keskmise tulemuse
print(f"Sinu parima hüppe tulemus on {parim_tulemus:.2f} meetrit.")  # kuvame parima tulemuse, ümardame kahe komakohani
print(f"Sinu keskmise hüppe tulemus on {keskmine_tulemus:.2f} meetrit.")  # kuvame keskmise tulemuse, ümardame kahe komakohani
# Lõpp

