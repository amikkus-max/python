# 3. Täringud
# 	kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
# 	kasutaja võistleb kahe täringuga arvuti vastu - 1p
# 	kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
# 	kood kommenteeritud - 1p

import random  # impordime random mooduli, et saaksime kasutada juhuslike arvude funktsioone

print("=== Täringumäng ===")  # programmi pealkiri
print("Tere tulemast täringumängu! Sa võistled kahe täringuga arvuti vastu.")
print("Mängu eesmärk on visata suurem täringupunktisumma kui arvuti.")
print("Kui võidad, saad laual oleva raha endale!")
print("Kui kaotad, saab arvuti rikkamaks")
print("Kui on viik, saate mõlemad oma panuse tagasi.")
print("may the odds be ever in your favor!")

try:  
	panus = int(input("Sisesta, kui palju raha soovid panustada (täisarv): "))  # küsime kasutajalt panuse
except:  # kui kasutaja ei sisesta int tüüpi numbrit, anname veateate. EI MINGEID SENTE! :D
	print("Panus peab olema ikka number!")	
else:
	if panus <= 0:  # kontrollime, et panus oleks positiivne täisarv
		print("Panus peab olema positiivne täisarv!")
	else: # kui panus on korrektne, jätkame mängu
		print(f"Sinu panus on {panus}.")
		
		# Viskame täringud
		kasutaja_t2ring1 = random.randint(1, 6)  # kasutaja esimene täring
		kasutaja_t2ring2 = random.randint(1, 6)  # kasutaja teine täring
		arvuti_t2ring1 = random.randint(1, 6)  # arvuti esimene täring
		arvuti_t2ring2 = random.randint(1, 6)  # arvuti teine täring
		
		# Arvutame punktisummad
		kasutaja_summa = kasutaja_t2ring1 + kasutaja_t2ring2
		arvuti_summa = arvuti_t2ring1 + arvuti_t2ring2
		
		# Kuvame tulemused
		print(f"Sinu täringud: {kasutaja_t2ring1} ja {kasutaja_t2ring2}, summa: {kasutaja_summa}")
		print(f"Arvuti täringud: {arvuti_t2ring1} ja {arvuti_t2ring2}, summa: {arvuti_summa}")
		
		# Määrame võitja
		if kasutaja_summa > arvuti_summa:
			print(f"Palju õnne! Sa võitsid {panus} rahaühikut!")
		elif kasutaja_summa < arvuti_summa:
			print(f"Kahjuks kaotasid. Arvuti võitis {panus} rahaühikut.")
		else:
			print("Viik! Saate mõlemad oma panuse tagasi.") 