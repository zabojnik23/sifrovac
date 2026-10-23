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


zprava = "ahoj svete"
tajne = zasifruj(zprava, 3, abeceda)
print("Zasifrovano:", tajne)