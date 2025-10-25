import turtle

try:
    r = float(input("Ringi raadius r="))
    s = 3.14 * r ** 2
    p = 2 * 3.14 * r
    print(f"Ringi pindala on {s:0.2f} ja ümbermõõt on {p:.2f}")
    turtle.circle(r)
except:
    print("Kontrolli sisestust!")

turtle.done()