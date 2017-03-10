import math

sutaziaci = {}
juniori = set()

def addpoints(meno, body):
    body = float(body) + sutaziaci.get(meno, 0)
    sutaziaci[meno] = body


def reducepoints(percento):
    for hrac in sutaziaci:
        body = sutaziaci[hrac]
        inverzne_percento = (1 - (float(percento) / 100))
        nove_body = math.floor(body * inverzne_percento)
        sutaziaci[hrac] = nove_body


def junior(meno):
    if meno in sutaziaci:
        juniori.add(meno)


def ranks(jr=None):
    vypisujem_vsetkych = True
    if jr and jr == "junior":
        vypisujem_vsetkych = False
    usortene = sorted(sutaziaci.items(), key=lambda x: x[1], reverse=True)
    for hrac, body in usortene:
        if vypisujem_vsetkych or hrac in juniori:
            print("Hrac {} ma {:g} bodov".format(hrac, body))


while True:
    command = input().split()
    if command[0] == "points":
        addpoints(*command[1:])

    elif command[0] == "reduce":
        reducepoints(*command[1:])

    elif command[0] == "junior":
        junior(*command[1:])

    elif command[0] == "ranking":
        ranks(*command[1:])

    elif command[0] == "quit":
        print("Goodbye")
        break
