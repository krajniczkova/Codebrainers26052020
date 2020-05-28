# Implementacja obiektowa

class Konto:
    def __init__(self, stan_poczatkowy, imie, nazwisko, numer):
        print("Jestem metodą __init__")
        # atrybuty obiektu:
        self.stan = stan_poczatkowy
        # atrybut obiektu o nazwie "stan"
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer = numer

    def wplac(self, kwota):
        self.stan += kwota

    def wyplac(self, kwota):
        if self.stan >= kwota:
            self.stan -= kwota
            return kwota
        else:
            raise Exception('Brak środków na koncie.')

    def pokaz_detale(self):
        # string = self.imie + "\t" + self.nazwisko + "\t" + str(self.stan) + "\t" + str(self.numer)
        string = f"{self.imie} {self.nazwisko} {self.stan} {self.numer}"
        # string = "{self.imie} {self.nazwisko} {self.stan} {self.numer}"-->obczić -->format
        return string

    def przelej(self, kwota, konto_odbiorcy):
        temp = self.wyplac(kwota)
        konto_odbiorcy.wplac(temp)


# Konto()-->obiekt
konto = Konto(0, 'Harry', 'Potter', 987654321)
print(konto)

print(konto.pokaz_detale())

konto1=Konto(100, 'Hermiona', 'Granger', 123456789)


konto.wplac(100)
print(konto.stan)
konto.wyplac(51)
print(konto.stan)
konto.przelej(2,konto1)
print(konto.pokaz_detale())
print(konto1.pokaz_detale())

"""
print(Konto(0, 'Magda','Krajnik',123456789).nazwisko)
print(Konto(0, 'Magda','Krajnik',123456789).stan)
print(Konto(0, 'Magda','Krajnik',123456789).numer)
"""
