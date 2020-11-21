if True: print("Igaz!")

print("Név: {0},Kor: {1}".format("Béla",24))
#helyörzők, helyettesítődnek a format fügvény paramétereivel.
#változókkal is működik.



név = "Géza"
kor = 12
print(f"Név: {név}, Kor: {kor}")
#f string.



print("Név: " + név + ", Kor:" + str(kor))
#nem szöveges változókat átkell alakítani szöveges típusra.
#ehhez az str azaz string függvény áll a rendelkezésünkre.



print(1,2,3, sep="/", end="---")
#a print függvény paraméterei között megadhatunk kulcsszavas paramétereket is.
#sep - nem az alapértelmezett szóköz legyen hanem egy másik karakter.
#end - utolsó karakterét szeretnénk megváltoztatni,akkor az end paramétert kell módosítanunk.



print("\n")

print("Hossz\tabb \n szöveg...") #\t - Tabulátor karakter , #\n - Sortörés karakter.
print("Hossz\tabb \n szö\\veg...") #a backslash "\" printeléséhez "\\"-t kell írni.
print(r"Hossz\tabb \n szö\\veg...") #az (r"szöveg")-vel nem értékeli ki.

print("\n")

def köszönés():
    print("Hello")

köszönés()
köszönés()
köszönés()

print("\n")

def melyik_a_nagyobb_szám(a,b):  #formális paraméterek
    if a > b:
        print(a,"nagyobb")
    elif b > a:
        print(b,"nagyobb")
    else:
        print(a,"és",b,"egyenlőek")

melyik_a_nagyobb_szám(12,24) #aktuális paraméterek

#a paraméter átadás sorrendben történik azaz a = 12 , b = 24
#a függvény fejlécében elhelyezett paramétereket : formális paramétereknek nevezzük
#az átadott változókat pedig : aktuális paramétereknek nevezzük

#természetesen alkalmazhatunk változókat is
#pl.:
#x = 12
#y = 24
#melyik_a_nagyobb_szám(x, y)

print("\n")

def nullázó_függvény(x):
    print("Ezt kaptuk kívülről:", x)
    x = 0
    print("Erre változtattuk:", x)


x = 12
nullázó_függvény(x)
print("Globális változó:", x)


def globális_nullázó_függvény():
    global x
    x = 0

globális_nullázó_függvény()
print("Globális változó:", x)


print("\n")


# szelekció - elágazások - if

szám = 236
futás = True

while futás == True:
    tipp = int(input("Milyen számra tipplesz?"))
    #print(type(tipp))

    if tipp == szám:
        print("Gratulálok, eltaláltad!")
        futás = False
    elif tipp < szám:
        print("A szám nagyobb!")
    else:
        print("A szám kisebb!")
else:
    print("Vége a programnak")


print("\n")

#alapértelmezett paraméter
#kulcsszavas paraméter átadás

def üzenet_sokszorozó(üzenet, szorzó = 3):
    print(üzenet*szorzó)

üzenet_sokszorozó("Hello ")
üzenet_sokszorozó("Hello ", 4)

print("\n")

def f(a, b=2 ,c=3):
    print(f"A={a},B={b},C={c}")

f(12)
f(11,12,13)
f(c=1,b=2,a=3)
f(3,2,1)

print("\n")

#változó számú paraméter átadása függvényeknek

def függvény(a=111, *számok, **mellékek ):
    print("A =", a)

    for szám in számok:
        print(szám)

    for kulcsszó, érték in mellékek.items():
        print(kulcsszó,érték)

függvény(222,1,2, Béla = 1234, Géza = 5678, Aladár = 1357)

print("\n")

#visszatérési értékkel rendelkező függvény - return kulccszó

def add_vissza_a_nagyobb_számot(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return"A két szám egyenlő!"

print(add_vissza_a_nagyobb_számot(12,45))

print("\n")

def üres_függvény_egyenlőre():
    '''Itt Lehet dokumentálni a függvényt! (DocStrings)'''

    pass # tehát egyenlőre még nem dolgozzuk ki a függvényt

print(üres_függvény_egyenlőre.__doc__)
help(üres_függvény_egyenlőre)

print("\n")


# modulok - modules

import sys
print("A parancssoros indításnál átadott paraméterek listája")
for i in sys.argv:
    print(i)

print("\n")

import os
print(os.getcwd())

print("\n")

import math
print("Négyzetgyök:", math.sqrt(16))

print("\n")

from math import sqrt
print("Négyzetgyök:", sqrt(16))

print("\n")

if __name__ == "__main__":
    print("Főprogramként futok")
else:
    print("Valahonnan importáltak, mint külső modul")

print("\n")

def saját_modul_függvénye():
    print("Importálható modul vagyok!")

__verison__ = "v1.7.0"

print("\n")

#adatstruktúrák - listák

bevásárlólista = ["liszt", "tej", "nutella"]
#print("Bevásárlólista:",bevásárlólista)

bevásárlólista.append("csoki")
bevásárlólista.sort()

for listaelem in bevásárlólista:
    print(listaelem)

print("Az első listaelem:", bevásárlólista[0])
del bevásárlólista[0]
print("Az első listaelem:", bevásárlólista[0])

print("\n")

# tuple (olyan, mint a lista, csak az elemei nem módosíthatóak)

állatok = ("kutya", "macska", "ló")
print(type(bevásárlólista))
print(type(állatok), len(állatok))

új_állatok = állatok, "tengerimalac","hal"
print(állatok, len(állatok))
print(új_állatok,len(új_állatok))
print(új_állatok[0][1])

print("\n")

# szótárak - dictionary

database = {
    "Adam" : "adam@gmail.com",
    "Peti" : "peti@gmail.com",
    "Viktor" : "viktor@gmail.com"
}

print("Before delete")
print("There is",len(database),"account left")
for név, email in database.items():
    print(név, email)


print("\n")

del database["Peti"]
print("After delete")
print("There is",len(database),"account left")

database["Adam"]="adamoss@gmail.com"

for név, email in database.items():
    print(név, email)

if "Peti" in database:
    print("Peti - nincs törölve!")
else:
    print("Peti - törölve!")

print("\n")

# halmazok - set

országok = ["USA", "UK", "Ausztria","Dánia","Dánia"]
országok_halmaza = set(országok)
print("Lista:", országok)
print("Halmaz:", országok_halmaza)
#print("Belgium" in országok_halmaza)

#A SET hasonló mint a tuple, elemei nem módosíthatóak, viszont egy elem csak egyszer szerepelhet benne!
#pl.: Dánia 2x van de a halmazban csak egyszer írja!
#copy függvénnyel másolatot hozhatunk a halmazból amit ezután módosíthatunk
több_ország_halmaz = országok_halmaza.copy()
több_ország_halmaz.add("Kína")

print("Részhalmaza?: ",több_ország_halmaz.issuperset(országok_halmaza)) # részhalmaza-e ?
országok_halmaza.remove("UK")
print(országok_halmaza & több_ország_halmaz) #metszet

print("\n")

#szekvenciák megcímezése

lista = ["alma","körte","kutya","macska","Nutella"]
csak_egy_szöveg = "Csak egy szöveg vagyok!"

print("Cs betűvel kezdődik?",csak_egy_szöveg.startswith("Cs"))
print("Benne van a szövegben az egy?","egy" in csak_egy_szöveg)
print("Hol található a vagyok?",csak_egy_szöveg.find("vagyok"))
elválasztó_karakter = " // "
print(elválasztó_karakter.join(lista))

print("\n")

lista_copy = lista #lista_copy = lista [:] - így kell másolni a listát!!!!

print(lista.index)
print(lista_copy.index)

del lista[0]
print(lista)
print(lista_copy)
#ugyanazt fogja mutatni mivel csak egy hivatkozás jön létre, tehát ha az elsőn változtatunk,
#akkor a második is változik

print()
print(lista[0])
print(lista[2])
print(lista[-1]) #hátulról az 1. elem
print(lista[-2]) #hátulról a 2. elem
print(csak_egy_szöveg[0])
print(csak_egy_szöveg[-1])
print()
print(lista[1:3])
print(lista[2:])
print(lista[:2])
print(lista[1:-1])
print(lista[:]) # a lista teljes elemeinek kiírása
print()
print(csak_egy_szöveg[2:8])
print(csak_egy_szöveg[1:-2:2]) #kettesével írja ki
print(csak_egy_szöveg[::-1]) #visszafelé
#print(csak_egy_szöveg[honnantól:meddig:hányasával])

print("\n")

#osztályok és objektuom

class Munkatárs:
    '''Munkatársak regisztrálása'''

    ennyi_munkatárs_lett_létrehozva = 0 #osztályváltozó, ebből csak egy van


    def __init__(self, munkatárs_név): #konstruktor - létrehozott függvény - speciális tagfüggvény, mellyel
        self.név = munkatárs_név       #létrehozhatjuk magát az osztály egy példányát.
        Munkatárs.ennyi_munkatárs_lett_létrehozva += 1 #ha létrehozunk egyet

    def köszönés(self):
        print(f"Hello én {self.név} vagyok.")

    def vége_a_műszaknak(self):
        Munkatárs.ennyi_munkatárs_lett_létrehozva -= 1 #hazament a munkából

    @classmethod
    def hányan_dolgoznak_még(cls):
        print(cls.ennyi_munkatárs_lett_létrehozva, " ember dolgozik még.") #cls magára a class-ra utal

#class - sablonok
#objektumok - példányok
#az objektumoknak és a sablonnak is lehetnek tulajdonságai amiket változókban tárolunk (__init__)
#és lehetnek képességei melyeket függvényben írunk le.
#osztályváltozókat és osztályfüggvényeket tehát közvetlenül az osztály segítségével külön objektumpéldányok
#létrehozások nélkül is használhatjuk.


egy_munkatárs = Munkatárs("Viktor")
egy_munkatárs.köszönés()
másik_munkatárs = Munkatárs("Ádám")
másik_munkatárs.köszönés()

Munkatárs.hányan_dolgoznak_még()
egy_munkatárs.vége_a_műszaknak()
Munkatárs.hányan_dolgoznak_még()
másik_munkatárs.vége_a_műszaknak()
Munkatárs.hányan_dolgoznak_még()

print("\n")

#fájlok olvasása és írása

valamilyen_többsoros_szöveg = '''\
Imagination is more important
than knowledge. Knowledge is limited.
Imagination encircles the world.
[Albert Einstein1]
'''

file = open("adatok.txt", "w") #"w" - write/írás , "r" - read/olvasás
file.write(valamilyen_többsoros_szöveg)
file.close()

file = open("adatok.txt", "r")
while True:
    egy_sor = file.read()
    if len(egy_sor) == 0:
        break
    print(egy_sor, end="")

file.close()

print("\n")

# bármilyen objektum tárolása

import pickle

ez_egy_lista = ["búbosvöcsök",999,False]

fájl = open("tároló.dat","wb") #eddig ugyanaz
pickle.dump(ez_egy_lista,fájl) #elraktuk
fájl.close()

del ez_egy_lista #kitöröltük

fájl = open("tároló.dat","rb")
ez_egy_másik_lista = pickle.load(fájl)
fájl.close()

print(ez_egy_másik_lista)

print("\n")

#with

with open("adatok.txt", "r") as fájl:
    for sor in fájl:
        print(sor, end="")
# nem szükséges a fájl lezárása

print("\n")

#kivételkezelés

class túl_kis_szám_kivétel(Exception):
    '''Akkor szól, ha túl kicsi a bevitt szám.'''
    def __init__(self, bevitt_szám, minimális_érték):
        Exception.__init__(self)
        self.bevitt_szám = bevitt_szám
        self.minimális_érték = minimális_érték

try:
    num = int(input("Enter the number: ")) #beolvassuk és konvertáljuk egész típussá
    if num < 100:
        raise túl_kis_szám_kivétel(num,100) #egy kivétel keletkezik
except túl_kis_szám_kivétel as TKSZK:
    print(f"A beírt szám {TKSZK.bevitt_szám},"
          f" A minimális érték: {TKSZK.minimális_érték}")
except ValueError:
    print("This is not a number!") #csak a ValueError hiba esetén
except:
    print("Something went wrong!") #bármilyen hiba esetén
else:
    print(f"So the number was: {num}") #ha nincs semmilyen hiba
finally:
    print("Good Bye!") #ezt mindenképpen lefogja futtatni
