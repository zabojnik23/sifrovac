abeceda="abcdefghijklmnopqrstuvwxyz"
def zasifruj(text, posun, abeceda):
    for i in range(len(zprava)):
            znak = zprava[i]
    
            if znak == " ":
                zasifrovana_zprava += " "
            else:
                puvodni_index = abeceda.index(znak)
                novy_index = (puvodni_index + posun) % len(abeceda)
                zasifrovana_zprava += abeceda[novy_index]
            return text

def desifruj(text, posun):
    # TODO (B): posuň každé písmeno o 'posun' míst dozadu
    return text


zprava = "ahoj svete"
tajne = zasifruj(zprava, 3, abeceda)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, 3))