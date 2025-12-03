#  Kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. 
#  Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, 
#  valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
#  Kõik kujundite joonistamise käsud peavad olema kirjutatud eraldi funktsioonidesse. 
#  Näiteks funktsioon joonista_ruut() või joonista_viisnurk(). 
#  Pärast joonistamist peab programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, 
#  jättes sisendi tühjaks.


# iseseisev töö nr3
# autor: Andrus Mikkus
# kuupäev: 03.12.2025

import turtle
import random
import math

def joonista_kolmnurk(suurus):
    for _ in range(3):
        turtle.forward(suurus)
        turtle.right(120)
def joonista_ruut(suurus):
    for _ in range(4):
        turtle.forward(suurus)
        turtle.right(90)
def joonista_viisnurk(suurus):
    for _ in range(5):
        turtle.forward(suurus/2)
        turtle.right(72)
def joonista_ring(suurus):
    turtle.circle(suurus/2)

kujundid = {1: "kolmnurk", 2: "ruut", 3: "viisnurk", 4: "ring", 5: "suvaline"}
joonista_kujund = {
    1: joonista_kolmnurk,
    2: joonista_ruut,
    3: joonista_viisnurk,
    4: joonista_ring
}
suurus = 100
screen = turtle.Screen()
screen.setup(width=0.75, height=0.75)
max_x = (screen.window_width() // 2) - suurus
max_y = (screen.window_height() // 2) - suurus
programmil6pp = False

while not programmil6pp:
    
    while not programmil6pp:
        print("Vali kujundi tüüp:")
        for key, value in kujundid.items():
            print(f"{key}: {value}")
        kujund = input("Sisesta kujundi number. Tühi väärtus lõpetab programmi töö: ")
        if kujund == "":
            programmil6pp = True
        elif kujund not in map(str, kujundid.keys()):
            print("Valik ei sobi, proovi uuesti.")
        else: 
            kujund = int(kujund)
            break

    while not programmil6pp:
        arv = input("Sisesta joonistatavate kujundite arv: ")
        if arv == "":
            programmil6pp = True
        elif not arv.isdigit() or int(arv) <= 0:
            print("Palun sisesta positiivne täisarv.")
        else:
            arv = int(arv)
            break

    turtle.clear()

    if not programmil6pp: 
        screen.tracer(0) 
        for _ in range(arv):
            if kujund == 5:
                kujundi_valik = random.randint(1, 4)
            else:
                kujundi_valik = kujund
            joonista = joonista_kujund[kujundi_valik]
            turtle.penup()
            turtle.goto(random.randint(-max_x, max_x), random.randint(-max_y, max_y))
            turtle.pendown()
            joonista(suurus)
        screen.tracer(1)