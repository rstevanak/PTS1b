import hashlib
import math
import uuid

sutaziaci = {}
juniori = set()

heslo = input("Zadajte heslo, ktore sa bude pouzivat:")
sol = uuid.uuid4().hex
hashovane_heslo = hashlib.sha512(str(heslo + sol).encode('utf-8')).hexdigest()


def kontrola_hesla(funkcia):
    def nova_funkcia(*args, **kwds):
        input_heslo = input("Zadajte heslo:")
        posolene_heslo = str(input_heslo + sol).encode('utf-8')
        if hashlib.sha512(posolene_heslo).hexdigest() == hashovane_heslo:
            funkcia(*args, **kwds)
        else:
            print("Zle heslo")
    return nova_funkcia

@kontrola_hesla
def addpoints(meno, body):
    body = float(body) + sutaziaci.get(meno, 0)
    sutaziaci[meno] = body

@kontrola_hesla
def reducepoints(percento):
    for hrac in sutaziaci:
        body = sutaziaci[hrac]
        inverzne_percento = (1 - (float(percento) / 100))
        nove_body = math.floor(body * inverzne_percento)
        sutaziaci[hrac] = nove_body

@kontrola_hesla
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


@kontrola_hesla
def koniec():
    print("Goodbye")
    quit()


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
        koniec()
    else:
        print("Nerozpoznany prikaz")
