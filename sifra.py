abeceda="abcdefghijklmnopqrstuvwxyz"
def zasifruj(text, posun, abeceda):
    zasifrovana_zprava = ""
    for i in range(len(text)):
        znak = text[i]
    
        if znak == " ":
            zasifrovana_zprava += " "
        else:
            puvodni_index = abeceda.index(znak)
            novy_index = (puvodni_index + posun) % len(abeceda)
            zasifrovana_zprava += abeceda[novy_index]
    return zasifrovana_zprava

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


zprava = "ahoj svete"
tajne = zasifruj(zprava, 3, abeceda)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, 3, abeceda))