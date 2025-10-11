import random
import turtle
#Harjutus 5

# Mündiviskamise äraarvamine koos juhuslikkusega (and ja or)
# Kirjuta programm, mis simuleerib mündiviskamist.
# Programm genereerib juhusliku tulemuse – “kiri” või “kull”, kasutades random.randint(0,1) funktsiooni.
# Programmi koostamisel pead importima import random mooduli ja kasutama randint() funktsiooni,
# et valida kahe võimaliku tulemuse vahel. Näiteks, kui randint(0, 1) annab tulemuseks 0,
# siis võib see tähendada “kirja”, ja 1 võib tähendada “kulli”.
# Seejärel palub programm kasutajal arvata, kumb külg maandub ülespoole.
# Kasuta if lauset, et kontrollida, kas kasutaja arvas õigesti. Kui arvas õigesti,
# siis joonista Turtle abil roheline ring; kui valesti, siis punane ring.
# 0 - kiri
# 1 - kull

# mynt = random.randint(0,1)
# t = turtle.circle(30)
# arvamus = int(input("Kas 0 või 1?"))
# if arvamus == mynt:
#     print("Läks täppi")
#     t.fillcolor("green")
# else:
#     print("Kahju :(")
#     turtle.circle(5)
#     t.fillcolor(red)
# print(mynt)


mynt = random.randint(0,1)
arvamus = input("kull või kiri: ")

turtle.color("green")
if mynt == 0 and arvamus == "kiri":
    turtle.circle(100)
    print("OK")
elif mynt == 1 and arvamus == "kull":
    print("OK")
else:
    turtle.color("red")
    turtle.circle(100)
    print("NotOK")


turtle.done()


# Matemaatika test (randint)
# Kirjuta programm, mis kontrollib kasutaja poolt sisestatud vastust lihtsale matemaatikaülesandele.
# Näiteks, programm esitab küsimuse “Mis on 3 korda 4?”.
# Kasutaja peab sisestama vastuse. Kui kasutaja vastus on 12, siis programm väljastab “Õige vastus!”,
# kui aga vastus on midagi muud, siis väljastab “Vale vastus, proovi uuesti!”.
# Kasuta if ja else lauseid selleks, et kontrollida kasutaja sisestatud vastust.


arv1 = random.randint(1,10)
arv2 = random.randint(1,10)
tehe = arv1 * arv2
vastus = int(input(f"{arv1} x {arv2} = "))
if vastus == tehe:
    print("Õige!")
else:
    print("Vale!")





#Vanusepiiranguga üritus
#
# Sa oled loomas programmi, mis aitab kontrollida,
# kas inimesed vastavad vanusepiirangu nõuetele üritusel osalemiseks.
# Programm palub kasutajal sisestada oma vanuse.
# Kui vanus on vähemalt 18 aastat, siis programm annab teada,
# et kasutaja võib üritusele siseneda. Kui vanus on alla 18, siis programm teatab,
# et üritusele sisenemiseks ei ole piisavalt vana.
# Kasuta if ja else lauseid, et luua see vanusekontrolli programm.

# vanus = int(input("Lisa vanus: "))
# if vanus>=18:
#     print("võib üritusele siseneda")
# else:
#     print("ei ole piisavalt vana")