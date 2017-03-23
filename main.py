import hashlib
import math
import uuid


class bezpecnost:
    """Trieda, ktora ma v sebe heslo a vie ho overovat"""
    __sol = None
    __heslo = None

    @staticmethod
    def nastavheslo():
        """Vypyta si a nastavi heslo pre subory"""
        input_heslo = input("Zadajte heslo, ktore sa bude pouzivat:")
        bezpecnost.__sol = uuid.uuid4().hex
        __heslo = str(input_heslo + bezpecnost.__sol).encode('utf-8')
        bezpecnost.__heslo = hashlib.sha512(__heslo).hexdigest()

    @staticmethod
    def kontrola_hesla(funkcia):
        """Dekorator, ktory si vypyta heslo, a ak je rovnake
         ako ulozene tak spusti funkciu"""
        def nova_funkcia(*args, **kwds):
            if not bezpecnost.__heslo or not bezpecnost.__sol:
                print("Nie je nastavene heslo")
            input_heslo = input("Zadajte heslo:")
            sol = bezpecnost.__sol
            spravne_heslo = bezpecnost.__heslo
            input_heslo = str(input_heslo + sol).encode('utf-8')
            if hashlib.sha512(input_heslo).hexdigest() == spravne_heslo:
                funkcia(*args, **kwds)
            else:
                print("Zle heslo")
        return nova_funkcia


class hodnotenia:
    """Trieda, ktora ma v sebe rebricek a vie s nim robit"""
    def __init__(self):
        self.sutaziaci = {}  # slovnik, kde je hrac:jeho pocet bodov
        self.juniori = set()  # mnoznina hracov, ktori su juniori
        self.heslo = bezpecnost()

    @bezpecnost.kontrola_hesla
    def addpoints(self, meno, body):
        """funkcia, ktora pripocita @body k bodom pre @meno, ak @meno este
        nie je v slovniku, tak ho prida a priradi mu @body"""
        body = float(body) + self.sutaziaci.get(meno, 0)
        self.sutaziaci[meno] = body

    @bezpecnost.kontrola_hesla
    def reducepoints(self, percento):
        """funkcia, ktora vsetkym hracom odpocita @percento % ich bodov
        a vysledok zaokruhli nadol na cele cisla"""
        for hrac in self.sutaziaci:
            body = self.sutaziaci[hrac]
            inverzne_percento = (1 - (float(percento) / 100))
            nove_body = math.floor(body * inverzne_percento)
            self.sutaziaci[hrac] = nove_body

    @bezpecnost.kontrola_hesla
    def junior(self, meno):
        """funkcia, ktora oznaci @meno hraca ako junior"""
        if meno in self.sutaziaci:
            self.juniori.add(meno)
        else:
            print("Taky hrac neexistuje")

    def ranks(self, jr=None):
        """funkcia, ktora vypise vsetkych hracov ak jr nie je zadane, alebo
        jr nie je "junior", inak vypise len hracov oznacenych ako junior"""
        vypisujem_vsetkych = True
        if jr and jr == "junior":
            vypisujem_vsetkych = False
        comp = lambda x: x[1]
        usortene = sorted(self.sutaziaci.items(), key=comp, reverse=True)
        if usortene:
            print("Hrac \t Body")
        for hrac, body in usortene:
            if vypisujem_vsetkych or hrac in self.juniori:
                print("{} \t {:g}".format(hrac, body))

    @bezpecnost.kontrola_hesla
    def koniec(self):
        """funkcia, ktora vypise "Goodbye" a ukonci program"""
        print("Goodbye")
        quit()

bezpecnost.nastavheslo()
instancia_body = hodnotenia()

# cyklus, ktory caka na prikaz, vykona ho a da sa ukoncit len cez koniec()
while True:
    command = input().split()
    if command[0] == "points":
        instancia_body.addpoints(*command[1:])

    elif command[0] == "reduce":
        instancia_body.reducepoints(*command[1:])

    elif command[0] == "junior":
        instancia_body.junior(*command[1:])

    elif command[0] == "ranking":
        instancia_body.ranks(*command[1:])

    elif command[0] == "quit":
        instancia_body.koniec()
    else:
        print("Nerozpoznany prikaz")
