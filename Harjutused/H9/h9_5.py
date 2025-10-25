# Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale.

for i in range(200, 320):  # vahemik 200 kuni 320
    if i % 7 == 0 and i % 5 != 0:  # jagub 7-ga, aga mitte 5-ga
        print(i, end=",")  # prindib numbri