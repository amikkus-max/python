#  Kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. 
#  Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, 
#  valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
#  Kõik kujundite joonistamise käsud peavad olema kirjutatud eraldi funktsioonidesse. 
#  Näiteks funktsioon joonista_ruut() või joonista_viisnurk(). 
#  Pärast joonistamist peab programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, 
#  jättes sisendi tühjaks.


# iseseisev töö nr3
# autor: Andrus Mikkus
# kuupäev: 27.10.2025

import turtle
import random
import math

# defineerime funktsioonid kujundite joonistamiseks
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
suurus = 100
programmil6pp = False


# while tsükkel, mis kestab seni, kuni programmil6pp saab True väärtuse.
# programmil6pp saab terve programmi käivitamise ajal True väärtuse siis, kui kasutaja sisestab tühja väärtuse.
# Laseb programmil mitu korda jooksutada
while not programmil6pp:
    
# while tsükkel kujundi küsimiseks
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

# while tsükkel joonistatavate kujundite arvu küsimiseks
    while not programmil6pp:
        arv = input("Sisesta joonistatavate kujundite arv: ")
        if arv == "":
            programmil6pp = True
        elif not arv.isdigit() or int(arv) <= 0:
            print("Palun sisesta positiivne täisarv.")
        else:
            arv = int(arv)
            break

# if tsükkel, mis joonistab kujundid, kui programmil6pp on False
    if not programmil6pp:
        turtle.speed(0)
        screen = turtle.Screen()
        screen.setup(width=0.75, height=0.75)
        for _ in range(arv):
            turtle.penup()
            turtle.goto(random.randint(-screen.window_width()//2 + suurus, screen.window_width()//2 - suurus),
                        random.randint(-screen.window_height()//2 + suurus, screen.window_height()//2 - suurus))
            turtle.pendown()
            if kujund == 1:
                joonista_kolmnurk(suurus)
            elif kujund == 2:
                joonista_ruut(suurus)
            elif kujund == 3:
                joonista_viisnurk(suurus)
            elif kujund == 4:
                joonista_ring(suurus)
            elif kujund == 5:
                juhuslik_valik = random.randint(1, 4)
                if juhuslik_valik == 1:
                    joonista_kolmnurk(suurus)
                elif juhuslik_valik == 2:
                    joonista_ruut(suurus)
                elif juhuslik_valik == 3:
                    joonista_viisnurk(suurus)
                elif juhuslik_valik == 4:
                    joonista_ring(suurus)

# tunnistan ausalt ülesse, kasutasin osade käskude puhul AI abi.
# kogu andmekogumike teema nõuab ka veel süvenemist ja aru saamist.