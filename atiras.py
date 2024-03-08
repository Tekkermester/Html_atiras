import time
file_name = ''
def adat_beolvasas():
    global file_name
    szoveg = ''
    while True:
        print("Adja meg a fálj helyét vagy másolja be a szöveget!"
              "\n      'masol' vagy 'hely' parancsal léphet tovább! [segítséghez: `!help` ]")
        m_h = str(input("> "))
        if m_h.lower() in ["masol", "másol"]:
            file_name = None
            print("Másolja ide a fálj tartalmát! ('megse' a kilépéshez) ")
            szoveg = str(input("> "))
            if szoveg.lower() in ["megse", "mégse"]:
                szoveg = ''
                print("Kilépés...")
            else:
                break
        elif m_h.lower() == "hely":
            print("Adja meg a fálj elérési útvonalát!")
            file_name = str(input("> "))
            if file_name.lower() in ["megse", "mégse"]:
                print("Kilépés...")
                file_name = None
            else:
                try:
                    with open(file_name, encoding = 'UTF-8') as file:
                        szoveg = file.read()
                        break
                except FileNotFoundError:
                    print("Hibás név vagy hely!")
                except FileExistsError:
                    print("Nincs ilyen fájl!")
                except IsADirectoryError:
                    print("Nem adtad meg a fájl nevét!")
        elif m_h.lower() == '!help':
            # segítség
            print("Segítséget a https://weboldal.com oldalon talál")
        else:
            print("Hibás bevitel! A 'masol' vagy a 'hely' parancsszavakat add meg!")
            file_name = None

    return szoveg


e_szoveg = None
html = None


def text_slice():
    szoveg = adat_beolvasas()
    global e_szoveg, html
    e_szoveg = szoveg
    # Check .html

    if file_name is not None:
        k = file_name.split('.')
        if k[1].lower() == 'html':
            html = True
        else:
            html = False
    else:
        html = False
    # A .slice() létezéséről ennek megírása után jöttem rá :(
    szavak = []
    if html:
        space_index = 0
        for i in szoveg:
            if i == '>':
                space_index = szoveg.index(i)
                elvalasztas = szoveg[:space_index]
                szavak.append(elvalasztas)
                uj_szoveg = szoveg[space_index + 1::]
                space_index = 0
                szoveg = uj_szoveg
        if uj_szoveg != '':
            szavak.append(uj_szoveg)
        uj_szoveg = ''
        szoveg2 = ''
        szavak2 = []
        for k in szavak:
            szoveg2 += k
            szoveg2 += ' '
        space_index = 0
        for i in szoveg2:
            if i == '<':
                space_index = szoveg2.index(i)
                elvalasztas = szoveg2[:space_index]
                szavak2.append(elvalasztas)
                uj_szoveg2 = szoveg2[space_index + 1::]
                space_index = 0
                szoveg2 = uj_szoveg2
        if uj_szoveg2 != '':
            szavak2.append(uj_szoveg2)
        uj_szoveg = ''
        szoveg3 = ''
        szavak3 = []
        for k in szavak2:
            szoveg3 += k
            szoveg3 += ' '
        space_index = 0
        for i in szoveg3:
            if i == ' ':
                space_index = szoveg3.index(i)
                elvalasztas = szoveg3[:space_index]
                szavak3.append(elvalasztas)
                uj_szoveg = szoveg3[space_index + 1::]
                space_index = 0
                szoveg3 = uj_szoveg
        if uj_szoveg != '':
            szavak3.append(uj_szoveg)
        uj_szoveg = ''
        szoveg4 = ''
        szavak4 = []
        for k in szavak3:
            szoveg4 += k
            szoveg4 += ' '
        space_index = 0
        for i in szoveg4:
            if i == '\"':
                space_index = szoveg4.index(i)
                elvalasztas = szoveg4[:space_index]
                szavak4.append(elvalasztas)
                uj_szoveg = szoveg4[space_index + 1::]
                space_index = 0
                szoveg4 = uj_szoveg
        if uj_szoveg != '':
            szavak4.append(uj_szoveg)
        szoveg5 = ''
        szavak5 = []
        for k in szavak4:
            szoveg5 += k
            szoveg5 += ' '
        szavak5 = szoveg5.split("\n")
        szoveg6 = ''
        szavak6 = []
        for k in szavak5:
            szoveg6 += k
            szoveg6 += ' '
        szavak6 = szoveg6.split()
        return szavak6
    elif html == False:
        space_index = 0
        uj_szoveg = ''
        for i in szoveg:
            if i == ' ':
                space_index = szoveg.index(i)
                elvalasztas = szoveg[:space_index]
                szavak.append(elvalasztas)
                uj_szoveg = szoveg[space_index + 1::]
                space_index = 0
                szoveg = uj_szoveg
        if uj_szoveg != '':
            szavak.append(uj_szoveg)
        return szavak


cserelt_szavak = {}


def karakter_csere():
    szavak = text_slice()
    if szavak == None:
        print('Nincsenek szavak a szövegben :(')
        ellenorzes()
    while True:
        print("Adja meg a kicserélendő karaktert!  (?? = '�') ")
        cserelendo = str(input("> "))
        if len(cserelendo) <= 2:
            if cserelendo == '??':
                cserelendo = '�'
            break
    volt_szo = []
    uj_szo = None
    for szo in szavak:
        for betu in szo:
            if (betu == cserelendo) and (szo not in volt_szo):
                jo_kar = False
                while jo_kar == False:
                    uj_karakter = input(f"{szo}: ")
                    volt_szo.append(szo)
                    if len(uj_karakter) <= 1:
                        rossz_szo = szo
                        uj_szo = szo.replace(betu, uj_karakter)
                        cserelt_szavak.update({rossz_szo: uj_szo})

                        jo_kar = True
                    else:
                        print("Csak egy karaktert adhatsz meg!")
    return cserelt_szavak


def ellenorzes():
    szoveg = ''
    cserelt_szavak = karakter_csere()
    print('')
    for i in cserelt_szavak.values():
        print(i, end=' * ')
    while True:
        print("\nHa szertne valamit javítani akkor az 'igen' parancsal léphet tovább! (kilépéshez enter) ")
        akar = input("> ")
        if akar.lower() == 'igen':
            while True:
                print("Írja be azt a szót karakter pontosan amelyet cserélni szertne! (kilépéshez ENTER) ")
                cserelendo = input("> ")
                try:
                    str(cserelendo)
                except:
                    print('Ez a szó nem található! (próbáld átmásolni :) )')
                if cserelendo == '':
                    break
                elif cserelendo in cserelt_szavak.values():
                    print("Írja be, hogy mire szeretné cserélni!")
                    uj = input("> ")
                    cserelt_szavak.update({cserelendo: uj})
                else:
                    print('Ez a szó nem található! (próbáld átmásolni :) )')

        else:
            print("Kilépés...")
            print()
            break
    global html,file_name, e_szoveg
    if (file_name == '' or file_name == None) and (html == False):
        for k, v in cserelt_szavak.items():
            e_szoveg = e_szoveg.replace(k, v)
        print(e_szoveg)
    else:
        file_atiras(cserelt_szavak)


def file_atiras(cserelt_szavak):
    global html, e_szoveg
    for k, v in cserelt_szavak.items():
        e_szoveg = e_szoveg.replace(k, v)
    with open(file_name, 'r+', encoding = 'UTF-8') as file:
        file.write(e_szoveg)
    print("A fálj átírva!")


while True:
    ellenorzes()
    print()
    akar = input("Kilépéshez ENTER, vagy 'ujra' a folytatáshoz:  ")
    if akar.lower() == 'ujra':
        ellenorzes()
    else:
        print("Kilépés...")
        time.sleep(1.5)
        break
