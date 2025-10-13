# 4. Emaili kontroll
# 	kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
# 	programm kontrollib kas email on sisestatud õigesti - vähemalt @-märgi kontroll - 1p
# 	programm tükeldab selle ja väljastab lause: ‘Tere enimi, sinu email on server serveris ja domeeniks on sul com’ - 1p
# 	kasutajalt küsitud küsimused on selgelt üheselt mõistetavad - 1p
# 	kood kommenteeritud - 1p



email = input("Palun sisesta oma emaili aadress kujul enimi.pnimi@server.xxx: ")  # küsime kasutajalt emaili aadressi
#email = "keegi.suva@ahv.ee"

# kontrollime, kas email on sisestatud õigesti, selles on ainult 1 @ märk ning 2 punkti  
if "@" not in email or email.count("@") > 1 or "." not in email or email.count(".") > 2:  
    print("See ei ole korrektne emaili aadress! Peab sisaldama ainult ühe @ märgi ning kaks punkti")
else:  # kui aadress korras, läheme edasi
    enimi, pnimi = email.split("@")[0].split(".")  # tükeldame emaili eesnimeks ja perekonnanimeks
    server, domeen = email.split("@")[1].split(".")  # tükeldame emaili serveriks ja domeeniks
    print(f"Tere \"{enimi}\", sinu email on server \"{server}\" ja domeeniks on sul \"{domeen}\"")  # kuvame tulemuse