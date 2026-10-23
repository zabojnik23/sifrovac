def desifruj(zasifrovana_zprava, posun, abeceda):
    desifrovana_zprava = ""
    for j in range(len(zasifrovana_zprava)):
        znak = zasifrovana_zprava[j]

        if znak == " ":
            desifrovana_zprava += " "
        else:
            puvodni_index = abeceda.index(znak)
            novy_index = (puvodni_index - posun) % len(abeceda)
            desifrovana_zprava += abeceda[novy_index]

    return desifrovana_zprava

zasifrovana_zprava = "dkrm vyhwh"
abeceda = "abcdefghijklmnopqrstuvwxyz"
#zprava = "ahoj svete"
#tajne = zasifruj(zprava, 3, abeceda)
#print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(zasifrovana_zprava, 3, abeceda))