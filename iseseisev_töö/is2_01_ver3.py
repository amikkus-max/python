# iseseisev töö nr2
# autor: Andrus Mikkus
# kuupäev: 27.10.2025

import turtle
import math

# skaleerimiseks muuda haara pikkust ja tipunurga suurust. 
# kolmnurkade arvu ning kilpkonna kiirust saab ka muuta. 
# use common sense

kilpkonna_kiirus = 3
haar = 300
tipunurk = 20
kolmnurkade_arv = 12

alus = math.sqrt(haar**2 + haar**2 - 2 * haar * haar * math.cos(math.radians(tipunurk)))
tipu_poorde_nurk = 180 - (360 / kolmnurkade_arv - tipunurk)
aluse_poorde_nurk = 180 - (180 - tipunurk) / 2
uus_kolmnurk = 180 + (360 / kolmnurkade_arv / 2) / 2 

print(uus_kolmnurk)

turtle.speed(kilpkonna_kiirus)
turtle.showturtle()
for _ in range(kolmnurkade_arv * 2):
    turtle.forward(haar)
    turtle.right(aluse_poorde_nurk)
    turtle.forward(alus)
    turtle.right(aluse_poorde_nurk)
    turtle.forward(haar)
    turtle.left(uus_kolmnurk)
turtle.done()