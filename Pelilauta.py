class Pelilauta:
    def __init__(self, a, b, c, d, e, f, g, h, i):
        self.lauta = [[a,b,c],[d,e,f],[g,h,i]]
        self.kierros = int()
        self.pelaajaMaara = int()
        self.pelitilanne = str()
        self.pelatutRuudut = list()

    def annapelaajaMaara(self): 
        return self.pelaajaMaara

    def asetaPelaajaMaara(self, pelaajaMaara): 
        self.pelaajaMaara = pelaajaMaara
    
    def annaPelitilanne(self): 
        return self.pelitilanne

    # Palauttaa tämänhetkisen pelitilanteen merkkijonona.
    def paivitaPelitilanne(self): 
        self.pelitilanne = "".join(f"{self.lauta[0][0]},{self.lauta[0][1]},{self.lauta[0][2]},{self.lauta[1][0]},{self.lauta[1][1]},{self.lauta[1][2]},{self.lauta[2][0]},{self.lauta[2][1]},{self.lauta[2][2]},{str(self.pelaajaMaara)},{str(self.kierros)}")

    # Palauttaa pelitilanteen lähtöasetelmiin, jossa ei asetettua pelaajamäärää ja kierros 1. 
    def nollaaPelitilanne(self):
        self.pelitilanne = "".join("1,2,3,4,5,6,7,8,9,0,1")
        self.asetaPelaajaMaara(0)
        self.asetaKierros(1)
        self.lauta[0][0] = '1' 
        self.lauta[0][1] = '2'
        self.lauta[0][2] = '3'
        self.lauta[1][0] = '4'
        self.lauta[1][1] = '5'
        self.lauta[1][2] = '6'
        self.lauta[2][0] = '7'
        self.lauta[2][1] = '8'
        self.lauta[2][2] = '9'
        self.pelatutRuudut.clear()
    
    def annaKierros(self):
        return self.kierros
    
    def asetaKierros(self, kierros):
        self.kierros = kierros

    # Tarkistaa jokaisen ruudun asetetun merkin varalta, ja lisää tällöin ruudun pelattujen ruutujen taulukkoon.
    def selvitaPelatutRuudut(self):
        if self.lauta[0][0] != '1': 
            self.pelatutRuudut.append(1)
        if self.lauta[0][1] != '2':
            self.pelatutRuudut.append(2)
        if self.lauta[0][2] != '3':
            self.pelatutRuudut.append(3)
        if self.lauta[1][0] != '4':
            self.pelatutRuudut.append(4)
        if self.lauta[1][1] != '5':
            self.pelatutRuudut.append(5)
        if self.lauta[1][2] != '6':
            self.pelatutRuudut.append(6)
        if self.lauta[2][0] != '7':
            self.pelatutRuudut.append(7)
        if self.lauta[2][1] != '8':
            self.pelatutRuudut.append(8)
        if self.lauta[2][2] != '9':
            self.pelatutRuudut.append(9)
    
    def annaPelatutRuudut(self):
        return self.pelatutRuudut

    # Tulostaa yksinkertaisen ristinolla-laudan komentoriville senhetkisen pelitilanteen mukaisesti. 
    def tulostaLauta(self):
        print("")
        print(self.lauta[0][0] + "|" + self.lauta[0][1] + "|" + self.lauta[0][2])
        print("-" + "+" + "-" + "+" + "-")
        print(self.lauta[1][0] + "|" + self.lauta[1][1] + "|" + self.lauta[1][2])
        print("-" + "+" + "-" + "+" + "-")
        print(self.lauta[2][0] + "|" + self.lauta[2][1] + "|" + self.lauta[2][2])
        print("")

    # Asetetaan oikea merkki kierroksen perusteella (pariton = X, parillinen = O) pelaajan antamaa lukua vastaavaan ruutuun.
    # Lisätään pelattu ruutu pelattujen ruutujen taulukkoon.
    # Kasvatetaan kierroksen lukua yhdellä.
    def asetaMerkki(self, numero): 
        if (self.kierros %2 == 1):
            merkki = 'X'
        else:
            merkki = 'O'
        if (numero == 1):
            self.lauta[0][0] = merkki
        if (numero == 2):
            self.lauta[0][1] = merkki
        if (numero == 3):
            self.lauta[0][2] = merkki
        if (numero == 4):
            self.lauta[1][0] = merkki
        if (numero == 5): 
            self.lauta[1][1] = merkki
        if (numero == 6): 
            self.lauta[1][2] = merkki
        if (numero == 7): 
            self.lauta[2][0] = merkki
        if (numero == 8): 
            self.lauta[2][1] = merkki
        if (numero == 9): 
            self.lauta[2][2] = merkki
        self.pelatutRuudut.append(numero)
        self.kierros = self.kierros + 1

    # Tulostetaan pelin lopputulos. Voiton tapauksessa voittaja selviää pelaajien määrän ja kierroksen avulla. Jos voittoa ei ole, julistetaan tasapeli.
    def julistaLopputulos(self):
        if self.onkoVoitto() == True: 
            if self.pelaajaMaara == 2: 
                if self.kierros %2 == 0:
                    print("Pelaaja 1 (X) voittaa!")
                else:
                    print("Pelaaja 2 (O) voittaa!")
            else:
                if (self.kierros %2 == 0):
                    print("Voitit pelin!")
                else:
                    print("Hävisit pelin!")
        else:
            print("Tasapeli!")

    # Palauttaa booleanin siitä, onko peli loppu. Voiton puuttuessa ja ruudukossa ollessa tilaa peli ei ole loppu.
    def peliLoppu(self):
        if self.onkoVoitto() == False and self.onkoTaynna() == False: 
            return False
        return True

    # Palautetaan boolean voitosta brute force -selvityksen perusteella siitä, että onko pelilaudalla sääntöjen mukaisesti kolmen merkin yhdistelmä.
    def onkoVoitto(self):
        if self.lauta[0][0] == self.lauta[0][1] and self.lauta[0][0] == self.lauta[0][2]: 
            return True
        if self.lauta[1][0] == self.lauta[1][1] and self.lauta[1][0] == self.lauta[1][2]: 
            return True
        if self.lauta[2][0] == self.lauta[2][1] and self.lauta[2][0] == self.lauta[2][2]:
            return True
        if self.lauta[0][0] == self.lauta[1][0] and self.lauta[0][0] == self.lauta[2][0]: 
            return True
        if self.lauta[0][1] == self.lauta[1][1] and self.lauta[0][1] == self.lauta[2][1]: 
            return True
        if self.lauta[0][2] == self.lauta[1][2] and self.lauta[0][2] == self.lauta[2][2]: 
            return True
        if self.lauta[0][0] == self.lauta[1][1] and self.lauta[0][0] == self.lauta[2][2]: 
            return True
        if self.lauta[0][2] == self.lauta[1][1] and self.lauta[0][2] == self.lauta[2][0]: 
            return True
        return False

    # Palautetaan boolean siitä, onko laudalla tilaa. Tarkistetaan ruutuja, kunnes jossain ruudussa ei ole merkkiä. Jos kaikissa ruuduissa merkki, lauta on täynnä.
    def onkoTaynna(self): 
        if self.lauta[0][0] != 'O' and self.lauta[0][0] != 'X': 
            return False
        if self.lauta[0][1] != 'O' and self.lauta[0][1] != 'X': 
            return False
        if self.lauta[0][2] != 'O' and self.lauta[0][2] != 'X': 
            return False
        if self.lauta[1][0] != 'O' and self.lauta[1][0] != 'X': 
            return False
        if self.lauta[1][1] != 'O' and self.lauta[1][1] != 'X': 
            return False
        if self.lauta[1][2] != 'O' and self.lauta[1][2] != 'X': 
            return False
        if self.lauta[2][0] != 'O' and self.lauta[2][0] != 'X': 
            return False
        if self.lauta[2][1] != 'O' and self.lauta[2][1] != 'X': 
            return False
        if self.lauta[2][2] != 'O' and self.lauta[2][2] != 'X': 
            return False
        return True