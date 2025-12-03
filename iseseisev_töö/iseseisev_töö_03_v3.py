import turtle
import random

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

joonista_dict = {
    1: {"name": "kolmnurk", "function": joonista_kolmnurk},
    2: {"name": "ruut",     "function": joonista_ruut},
    3: {"name": "viisnurk", "function": joonista_viisnurk},
    4: {"name": "ring",     "function": joonista_ring},
    5: {"name": "suvaline", "function": None}
}

suurus      = 100
screen      = turtle.Screen()
screen.setup(width=0.75, height=0.75)
max_x       = (screen.window_width() // 2) - suurus
max_y       = (screen.window_height() // 2) - suurus
endprogram  = False

while not endprogram:

    while not endprogram:
        print("Vali kujundi tüüp:")
        for valik, kujundi_valik_dict in joonista_dict.items():
            print(f"{valik} : {kujundi_valik_dict["name"]}")
        userchoice = input("Sisesta number: ")
        if userchoice == "":
            endprogram = True
        elif userchoice not in map(str, joonista_dict.keys()):
            print("See valik ei sobi")
        else:
            userchoice = int(userchoice)
            break

    while not endprogram:
        kujundite_arv = input("Kui mitu kujundit joonistada?: ")
        if kujundite_arv == "":
            endprogram = True
        elif not kujundite_arv.isdigit() or int(kujundite_arv) <= 0:
            print("Palun sisesta positiivne number")
        else:
            kujundite_arv = int(kujundite_arv)
            break

    if not endprogram: 
        turtle.clear()
        screen.tracer(0) 
        for _ in range(kujundite_arv):
            if userchoice == 5:
                joonista_kujund = random.randint(1, 4)
            else:
                joonista_kujund = userchoice
            joonista = joonista_dict[joonista_kujund]["function"]
            turtle.penup()
            turtle.goto(random.randint(-max_x, max_x), random.randint(-max_y, max_y))
            turtle.pendown()
            joonista(suurus)
        screen.tracer(1) 