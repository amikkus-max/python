# Harjutus 6
import turtle
import math

# Kasuta Python Turtles’i, et joonistada stseen, kus redel toetub majale 53° nurga all.
# Redeli ülemine ots peaks ulatuma 4,4 meetri kõrgusele maja seinal virtuaalses mõõtkavas.
# Muuda nurgad radiaanideks (radian)
# Redeli kaugus seinast: kasuta tangensfunktsiooni (tan) ja antud nurka, et leida, kui kaugele redeli alumine ots on seinast.
# Valem:
# Kaugus = Kõrgus seinaltan⁡(Nurk) 
# Redeli pikkus: kasuta Pythagorase teoreemi, et leida redeli pikkus, kui tead redeli kõrgust seinal ja kaugust seinast.
# Valem:
# Pikkus=(Ko˜rgus seinal)2+(Kaugus seinast)2 
# Ümarda vastus 2 komakohta
# Kuva vastused konsoolid

nurk = 53
k6rgus = 4.4
radiaanid = math.radians(nurk)
kaugus = k6rgus / math.tan(radiaanid)
# hypotenuus = math.sqrt(k6rgus**2 + kaugus**2)
hypotenuus = math.hypot(k6rgus, kaugus)


h = 50
turtle.fd(kaugus*h)
turtle.lt(90)
turtle.fd(k6rgus*h)
turtle.lt(143)
turtle.fd(hypotenuus*h)


print(radiaanid)
print(kaugus)
print(hypotenuus)
