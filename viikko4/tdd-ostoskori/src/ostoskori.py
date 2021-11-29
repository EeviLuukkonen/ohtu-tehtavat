from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []
        self.tavaroita = 0
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self.tavaroita
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0 
        for tuote in self.kori:
            summa += tuote.hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        self.tavaroita += 1
        ostos = Ostos(lisattava)
        for tuote in self.kori:
            if tuote.tuotteen_nimi() == ostos.tuotteen_nimi():
                tuote.muuta_lukumaaraa(1)
                return
        self.kori.append(ostos)


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for tuote in self.kori:
            if tuote.tuotteen_nimi() == poistettava.nimi():
                tuote.muuta_lukumaaraa(-1)
                if tuote.lukumaara() == 0:
                    self.kori.remove(tuote)

    def tyhjenna(self):
        self.kori = []
        self.tavaroita = 0
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
