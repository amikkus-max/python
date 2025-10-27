# iseseisev töö nr2
# autor: Andrus Mikkus
# kuupäev: 27.10.2025

import turtle
import math

# skaleerimiseks muuda haara pikkust ja tipunurga suurust. kilpkonna kiirust saab ka muuta. use common sense

kilpkonna_kiirus = 0
haar = 350
tipunurk = 72

alus = math.sqrt(haar**2 + haar**2 - 2 * haar * haar * math.cos(math.radians(tipunurk)))
tipu_poorde_nurk = 180 - (72 - tipunurk)
aluse_poorde_nurk = 180 - (180 - tipunurk) / 2

turtle.speed(kilpkonna_kiirus)
turtle.showturtle()
for _ in range(5):
    turtle.forward(haar)
    turtle.right(aluse_poorde_nurk)
    turtle.forward(alus)
    turtle.right(aluse_poorde_nurk)
    turtle.forward(haar)
    turtle.left(tipu_poorde_nurk)
turtle.right(36)
for _ in range(5):
    turtle.forward(haar)
    turtle.right(aluse_poorde_nurk)
    turtle.forward(alus)
    turtle.right(aluse_poorde_nurk)
    turtle.forward(haar)
    turtle.left(tipu_poorde_nurk)
turtle.done()