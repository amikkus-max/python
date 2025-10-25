# Harjutus 09

for i in range(1,42):
    if   i%15 == 0:
        print(i, "TIKTAK")
    elif i%5 == 0:
        print(i, "TAK")
    elif i%3 == 0:
        print(i, "TIK")
    else:
        print(i, end=" ")