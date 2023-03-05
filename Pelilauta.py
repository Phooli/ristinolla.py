class pelilauta:
    def __init__(self, a, b, c, d, e, f, g, h, i):
        self.lauta = [[a,b,c],[d,e,f],[g,h,i]]
        self.kierros = int()
        self.pelaajamaara = int()
        self.pelitilanne = str()
        self.pelatut_ruudut = list()

    # Palauttaa tämänhetkisen pelitilanteen merkkijonona.
    def paivita_pelitilanne(self): 
        self.pelitilanne = "".join(
            f"{self.lauta[0][0]},"
            f"{self.lauta[0][1]},"
            f"{self.lauta[0][2]},"
            f"{self.lauta[1][0]},"
            f"{self.lauta[1][1]},"
            f"{self.lauta[1][2]},"
            f"{self.lauta[2][0]},"
            f"{self.lauta[2][1]},"
            f"{self.lauta[2][2]},"
            f"{str(self.pelaajamaara)},"
            f"{str(self.kierros)}")

    # Palauttaa pelitilanteen lähtöasetelmiin, jossa ei asetettua pelaajamäärää ja kierros 1. 
    def nollaa_pelitilanne(self):
        self.pelitilanne = "".join("1,2,3,4,5,6,7,8,9,0,1")
        self.pelaajamaara = 0
        self.kierros = 1
        self.lauta[0][0] = '1' 
        self.lauta[0][1] = '2'
        self.lauta[0][2] = '3'
        self.lauta[1][0] = '4'
        self.lauta[1][1] = '5'
        self.lauta[1][2] = '6'
        self.lauta[2][0] = '7'
        self.lauta[2][1] = '8'
        self.lauta[2][2] = '9'
        self.pelatut_ruudut.clear()
    
    # Tarkistaa jokaisen ruudun asetetun merkin varalta, ja lisää tällöin ruudun pelattujen ruutujen taulukkoon.
    def selvita_pelatut_ruudut(self):
        if self.lauta[0][0] != '1': 
            self.pelatut_ruudut.append(1)
        if self.lauta[0][1] != '2':
            self.pelatut_ruudut.append(2)
        if self.lauta[0][2] != '3':
            self.pelatut_ruudut.append(3)
        if self.lauta[1][0] != '4':
            self.pelatut_ruudut.append(4)
        if self.lauta[1][1] != '5':
            self.pelatut_ruudut.append(5)
        if self.lauta[1][2] != '6':
            self.pelatut_ruudut.append(6)
        if self.lauta[2][0] != '7':
            self.pelatut_ruudut.append(7)
        if self.lauta[2][1] != '8':
            self.pelatut_ruudut.append(8)
        if self.lauta[2][2] != '9':
            self.pelatut_ruudut.append(9)
    
    # Tulostaa yksinkertaisen ristinolla-laudan komentoriville senhetkisen pelitilanteen mukaisesti. 
    def tulosta_lauta(self):
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
    def aseta_merkki(self, numero): 
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
        self.pelatut_ruudut.append(numero)
        self.kierros = self.kierros + 1

    # Tulostetaan pelin lopputulos. Voiton tapauksessa voittaja selviää pelaajien määrän ja kierroksen avulla. Jos voittoa ei ole, julistetaan tasapeli.
    def julista_lopputulos(self):
        if self.onko_voitto() == True: 
            if self.pelaajamaara == 2: 
                if self.kierros %2 == 0:
                    print("Pelaaja 1 (X) voittaa!\n")
                else:
                    print("Pelaaja 2 (O) voittaa!\n")
            else:
                if (self.kierros %2 == 0):
                    print("Voitit pelin!\n")
                else:
                    print("Hävisit pelin!\n")
        else:
            print("Tasapeli!\n")

    # Palauttaa booleanin siitä, onko peli loppu. Voiton puuttuessa ja ruudukossa ollessa tilaa peli ei ole loppu.
    def peli_loppu(self):
        if self.onko_voitto() == False and self.onko_taynna() == False: 
            return False
        return True

    # Palautetaan boolean voitosta selvittämällä, että onko pelilaudalla kolmen saman merkin jono.
    def onko_voitto(self):
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

    # Palauttaa sellaista ruutua vastaavan numeron, jolla jompikumpi pelaaja voittaisi. Jos sellaista ruutua ei ole, palautetaan 0.
    # Etsitään siis joka riviltä/diagonaalilta tilannetta, että olisi kaksi samaa merkkiä ja yksi tyhjä ruutu.
    def selvita_voittava_ruutu(self):
        voittava_ruutu = 0
        if self.lauta[0][0] == self.lauta[0][1] and self.lauta[0][2] == '3':
            voittava_ruutu = 3
            return voittava_ruutu
        if self.lauta[1][0] == self.lauta[1][1] and self.lauta[1][2] == '6':
            voittava_ruutu = 6
            return voittava_ruutu
        if self.lauta[2][0] == self.lauta[2][1] and self.lauta[2][2] == '9':
            voittava_ruutu = 9
            return voittava_ruutu
        if self.lauta[0][1] == self.lauta[0][2] and self.lauta[0][0] == '1':
            voittava_ruutu = 1
            return voittava_ruutu
        if self.lauta[1][1] == self.lauta[1][2] and self.lauta[1][0] == '4':
            voittava_ruutu = 4
            return voittava_ruutu
        if self.lauta[2][1] == self.lauta[2][2] and self.lauta[2][0] == '7':
            voittava_ruutu = 7
            return voittava_ruutu
        if self.lauta[0][0] == self.lauta[0][2] and self.lauta[0][1] == '2':
            voittava_ruutu = 2
            return voittava_ruutu
        if self.lauta[1][0] == self.lauta[1][2] and self.lauta[1][1] == '5':
            voittava_ruutu = 5
            return voittava_ruutu
        if self.lauta[2][0] == self.lauta[2][2] and self.lauta[2][1] == '8':
            voittava_ruutu = 8
            return voittava_ruutu
        if self.lauta[1][2] == self.lauta[2][2] and self.lauta[0][2] == '3':
            voittava_ruutu = 3
            return voittava_ruutu
        if self.lauta[0][2] == self.lauta[2][2] and self.lauta[1][2] == '6':
            voittava_ruutu = 6
            return voittava_ruutu
        if self.lauta[0][2] == self.lauta[1][2] and self.lauta[2][2] == '9':
            voittava_ruutu = 9
            return voittava_ruutu
        if self.lauta[1][0] == self.lauta[2][0] and self.lauta[0][0] == '1':
            voittava_ruutu = 1
            return voittava_ruutu
        if self.lauta[0][0] == self.lauta[2][0] and self.lauta[1][0] == '4':
            voittava_ruutu = 4
            return voittava_ruutu
        if self.lauta[0][0] == self.lauta[1][0] and self.lauta[2][0] == '7':
            voittava_ruutu = 7
            return voittava_ruutu
        if self.lauta[1][1] == self.lauta[2][1] and self.lauta[0][1] == '2':
            voittava_ruutu = 2
            return voittava_ruutu
        if self.lauta[0][1] == self.lauta[2][1] and self.lauta[1][1] == '5':
            voittava_ruutu = 5
            return voittava_ruutu
        if self.lauta[0][1] == self.lauta[1][1] and self.lauta[2][1] == '8':
            voittava_ruutu = 8
            return voittava_ruutu
        if self.lauta[0][0] == self.lauta[1][1] and self.lauta[2][2] == '9':
            voittava_ruutu = 9
            return voittava_ruutu
        if self.lauta[1][1] == self.lauta[2][2] and self.lauta[0][0] == '1':
            voittava_ruutu = 1
            return voittava_ruutu
        if self.lauta[0][0] == self.lauta[2][2] and self.lauta[1][1] == '5':
            voittava_ruutu = 5
            return voittava_ruutu
        if self.lauta[0][2] == self.lauta[1][1] and self.lauta[2][0] == '7':
            voittava_ruutu = 7
            return voittava_ruutu
        if self.lauta[0][2] == self.lauta[2][0] and self.lauta[1][1] == '5':
            voittava_ruutu = 5
            return voittava_ruutu
        if self.lauta[2][0] == self.lauta[1][1] and self.lauta[0][2] == '3':
            voittava_ruutu = 3
            return voittava_ruutu
        return voittava_ruutu

    # Palautetaan boolean siitä, että onko laudalla tilaa. Tarkistetaan ruutuja, kunnes jossain ruudussa ei ole merkkiä. Jos kaikissa ruuduissa merkki, lauta on täynnä.
    def onko_taynna(self): 
        if self.lauta[0][0] == '1':
            return False
        if self.lauta[0][1] == '2':
            return False
        if self.lauta[0][2] == '3':
            return False
        if self.lauta[1][0] == '4':
            return False
        if self.lauta[1][1] == '5':
            return False
        if self.lauta[1][2] == '6':
            return False
        if self.lauta[2][0] == '7':
            return False
        if self.lauta[2][1] == '8':
            return False
        if self.lauta[2][2] == '9':
            return False
        return True