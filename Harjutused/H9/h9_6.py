# Kuva nimekirjast unikaalsed nimed:
# nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']

nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
unikaalsed_nimed = set(nimed) # teeb uue unikaalsete nimede hulga käsuga set()
for nimi in unikaalsed_nimed:  # läbib iga unikaalse nime
    if nimed.count(nimi) > 1:  # kui nimi esineb rohkem kui korra hulgas nimed
        print(nimi)  # prindib nime