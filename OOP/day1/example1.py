konto={
    'imie': 'Artur',
    'nazwisko':'Siepietowski',
    'stan':0,
    'numer_telefonu':123456789
}

def wplac(kwota, _konto):
    _konto['stan']+=kwota

def pokaz_detale(_konto):
    print(_konto['imie'],_konto['nazwisko'])
    print(_konto['stan'])

print(konto)
wplac(100,konto)
print(konto)

konto1={
    'imie': 'Magdalena',
    'nazwisko':'Krajnik',
    'stan':1000,
}

def wyplac(kwota, _konto):
    if _konto['stan']>kwota:
        _konto['stan']-=kwota
        return kwota
    else:
        raise Exception('Nie masz wystarczających środków na koncie.')

print(wyplac(999,konto1))
print(konto1)
#print(wyplac(2,konto1))

def wyplac_bankomat(kwota,_konto):
    try:
        return wyplac(kwota,_konto)
    except Exception:
        print("EKRAN BANKOMATU: Brak środków")

def przelej(kwota,konto_nadawcy, konto_odbiorcy):
    try:
        temp=wyplac(kwota,konto_nadawcy)
        wplac(temp, konto_odbiorcy)
    except Exception:
        print("EKRAN STRONY INTERNETOWEJ: Brak środków do przelewu")

przelej(50, konto, konto1)
print(konto)
print(konto1)

przelej(500, konto, konto1)
print(konto)
print(konto1)