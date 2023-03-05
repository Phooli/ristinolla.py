import Pelilauta
import Pelaaja
import time
import random

class ristinolla:
    def __init__(self):
        self.pelilauta = Pelilauta.pelilauta('1','2','3','4','5','6','7','8','9',)
        self.Pelaaja1 = Pelaaja.ihmispelaaja()
        self.Pelaaja2 = Pelaaja

    def pelaa(self):

        # Jos kierron on muu kuin 1, ollaan ladattu tallennettu peli. Tällöin kysytään halukkuutta jatkaa peliä.
        # Jos jatketaan, peli jatkuu tallennetusta kohdasta automaattisesti.
        # Jos ei jatketa, nollataan pelitilanne, jolloin jatketaan uuden pelin pelaajamäärän selvittämisellä. 
        if self.pelilauta.kierros in (2,3,4,5,6,7,8,9): 
            jatketaankoTallennuksesta = input("Haluatko jatkaa tallennettua peliä? (Syötä K/E): ")
            if jatketaankoTallennuksesta == 'K' or jatketaankoTallennuksesta == 'k': 
                print("Jatketaan tallennettua peliä...")
                time.sleep(3)
            else: 
                self.pelilauta.nollaa_pelitilanne()

        # Jos pelaajamäärää ei asetettu, kysytään ihmispelaajien määrää. 1 = Pelaaja 2 on tietokonepelaaja. 2 = Pelaaja 2 on toinen ihmispelaaja.
        while self.pelilauta.pelaajamaara not in (1,2):
            try: 
                self.pelilauta.pelaajamaara = int(input("Aloitetaan uusi peli. Syötä ihmispelaajien määrä (1/2) "))
                if self.pelilauta.pelaajamaara < 1 or self.pelilauta.pelaajamaara > 2: 
                    print("Syötetty pelaajamäärä ei kelpaa.\n")
                    continue
            except ValueError:
                print("Syötteesi ei ole sopiva numero.\n")
            if self.pelilauta.pelaajamaara == 1: 
                self.Pelaaja2 = Pelaaja.tietokonepelaaja()
                print("Arvotaan aloittaja...\n")
                self.pelilauta.kierros = random.choice([1,2])
                time.sleep(3)
                if (self.pelilauta.kierros == 1):
                    print("Sinä (X) aloitat!")
                else:
                    print("Tietokonepelaaja (O) aloittaa!")
            if self.pelilauta.pelaajamaara == 2: 
                self.Pelaaja2 = Pelaaja.ihmispelaaja()

        # Kunnes peli ei ole päättynyt, pelaajat pelaavat vuorotellen meneillään olevan kierroksen(vuoron) perusteella. Tallennetaan peli joka vuoron jälkeen.
        while self.pelilauta.peli_loppu() == False: 
            if self.pelilauta.kierros % 2 == 1: 
                self.Pelaaja1.pelaa(self.pelilauta)
                self.tallenna()
            if self.pelilauta.peli_loppu() == False: 
                if self.pelilauta.kierros %2 != 1: 
                    self.Pelaaja2.pelaa(self.pelilauta)
                    self.tallenna()

        # Pelin loputtua tulostetaan lauta, julistetaan lopputulos, ja nollataan pelitilanne sekä keskeneräisen pelin tallennukset.
        self.pelilauta.tulosta_lauta()
        self.pelilauta.julista_lopputulos()
        self.pelilauta.nollaa_pelitilanne()
        self.tallenna()

    # Kirjoitetaan pelitilanne-merkkijono tallennus.txt-tiedostoon.
    def tallenna(self):
        try:
            tallennus = open("tallennus.txt", "w")
            tallennus.write(self.pelilauta.pelitilanne)
            tallennus.close()
        except Exception:
            print("Pelin tallennus ei onnistunut!\n")

    # Ladataan peli, eli luetaan tallennus.txt-tiedosto ja luodaan sen perusteella pelilauta, asetetaan pelaajamäärä, pelaajamäärän perusteella luodaan pelaajat,
    # asetetaan meneillään oleva kierros oikeaksi, ja selvitetään pelatut ruudut taulukkoon, jotta saadaan pelaajilta sopivat syötteet.
    def lataa(self): 
        try:
            tallennus = open("tallennus.txt", "r")
            tallenne = tallennus.read()
            tallennus.close()
            self.pelilauta = Pelilauta.pelilauta(tallenne[0], tallenne[2], tallenne[4], tallenne[6], tallenne[8], tallenne[10], tallenne[12], tallenne[14], tallenne[16]) 
            self.pelilauta.pelaajamaara = int(tallenne[18])
            if self.pelilauta.pelaajamaara == 1: 
                self.Pelaaja2 = Pelaaja.tietokonepelaaja()
            else: 
                self.Pelaaja2 = Pelaaja.ihmispelaaja()
            self.pelilauta.kierros = int(tallenne[20])
            self.pelilauta.selvita_pelatut_ruudut()
        except FileNotFoundError:
            print("Tallennettua peliä ei löytynyt!\n")
            self.pelilauta.nollaa_pelitilanne()

Peli = ristinolla()
Peli.lataa()
Peli.pelaa()