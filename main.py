import math

sutaziaci = {}
juniori = set()

while True:
    command = input().split()
    if command[0] == "points":
        body = sutaziaci.get(command[1], 0) + float(command[2])
        sutaziaci[command[1]] = body

    elif command[0] == "reduce":
        for hrac in sutaziaci:
            body = sutaziaci[hrac]
            inverzne_percento = (1 - (float(command[1]) / 100))
            nove_body = math.floor(body * inverzne_percento)
            sutaziaci[hrac] = nove_body

    elif command[0] == "junior":
        if command[1] in sutaziaci:
            juniori.add(command[1])

    elif command[0] == "ranking":
        vypisujem_vsetkych = True
        if len(command) > 1 and command[1] == "junior":
            vypisujem_vsetkych = False
        usortene = sorted(sutaziaci.items(), key=lambda x: x[1], reverse=True)
        for hrac, body in usortene:
            if vypisujem_vsetkych or hrac in juniori:
                print("Hrac {} ma {:g} bodov".format(hrac, body))

    elif command[0] == "quit":
        print("Goodbye")
        break
