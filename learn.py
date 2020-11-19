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
print("\n")

def köszönés():
    print("Hello")

köszönés()
köszönés()
köszönés()

print("\n")
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
