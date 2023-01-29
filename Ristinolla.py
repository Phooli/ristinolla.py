import Pelilauta
import Pelaaja
import time

class ristinolla:
    def __init__(self):
        self.pelilauta = Pelilauta.pelilauta('1','2','3','4','5','6','7','8','9',)
        self.Pelaaja1 = Pelaaja.ihmispelaaja()
        self.Pelaaja2 = Pelaaja

    def pelaa(self):
        if self.pelilauta.anna_kierros() != 1: 
            jatketaankoTallennuksesta = input("Haluatko jatkaa tallennettua peliä? (Syötä K/E): ")
            if jatketaankoTallennuksesta == 'K' or jatketaankoTallennuksesta == 'k': 
                print("Jatketaan tallennettua peliä...")
                try: 
                    time.sleep(3)
                except Exception:
                    print("Jokin meni pieleen!")
            else: 
                self.pelilauta.nollaa_pelitilanne()

        # Jos pelaajamäärää ei asetettu, kysytään ihmispelaajien määrää. 1 = Pelaaja 2 on tietokonepelaaja. 2 = Pelaaja 2 on toinen ihmispelaaja.
        while self.pelilauta.anna_pelaajamaara() != 1 and self.pelilauta.anna_pelaajamaara() != 2: 
            try: 
                self.pelilauta.aseta_pelaajamaara(int(input("Syötä ihmispelaajien määrä (1/2) ")))
                if self.pelilauta.anna_pelaajamaara() < 1 or self.pelilauta.anna_pelaajamaara() > 2: 
                    print("Syötetty pelaajamäärä ei kelpaa.\n")
                    continue
            except ValueError:
                print("Syötteesi ei ole sopiva numero.\n")
            if self.pelilauta.anna_pelaajamaara() == 1: 
                self.Pelaaja2 = Pelaaja.tietokonepelaaja()
            else: 
                self.Pelaaja2 = Pelaaja.ihmispelaaja()

        # Kunnes peli ei ole päättynyt, pelaajat pelaavat vuorotellen meneillään olevan kierroksen(vuoron) perusteella. Tallennetaan peli joka vuoron jälkeen.
        while self.pelilauta.peli_loppu() == False: 
            if self.pelilauta.anna_kierros() % 2 == 1: 
                self.Pelaaja1.pelaa(self.pelilauta)
                try:
                    self.tallenna()
                except Exception:
                    print("Jokin meni pieleen!")
            if self.pelilauta.peli_loppu() == False: 
                if self.pelilauta.anna_kierros() %2 != 1: 
                    self.Pelaaja2.pelaa(self.pelilauta)
                    try: 
                        self.tallenna()
                    except Exception:
                        print("Jokin meni pieleen!")

        # Pelin loputtua tulostetaan lauta, julistetaan lopputulos, ja nollataan pelitilanne sekä keskeneräisen pelin tallennukset. Suljetaan scannerit.
        self.pelilauta.tulosta_lauta()
        self.pelilauta.julista_lopputulos()
        self.pelilauta.nollaa_pelitilanne()
        try:  
            self.tallenna()
        except Exception:
            print("Jokin meni pieleen!")

    # Kirjoitetaan pelitilanne-merkkijono tallennus.txt-tiedostoon.
    def tallenna(self):
        tallennus = open("tallennus.txt", "w")
        tallennus.write(self.pelilauta.anna_pelitilanne())
        tallennus.close()

    # Ladataan peli, eli luetaan tallennus.txt-tiedosto ja luodaan sen perusteella pelilauta, asetetaan pelaajamäärä, pelaajamäärän perusteella luodaan pelaajat,
    # asetetaan meneillään oleva kierros oikeaksi, ja selvitetään pelatut ruudut taulukkoon, jotta saadaan pelaajilta sopivat syötteet.
    def lataa(self): 
        tallennus = open("tallennus.txt", "r")
        tallenne = tallennus.read()
        tallennus.close()
        self.pelilauta = Pelilauta.pelilauta(tallenne[0], tallenne[2], tallenne[4], tallenne[6], tallenne[8], tallenne[10], tallenne[12], tallenne[14], tallenne[16]) 
        self.pelilauta.aseta_pelaajamaara(int(tallenne[18]))
        if self.pelilauta.anna_pelaajamaara() == 1: 
            self.Pelaaja2 = Pelaaja.tietokonepelaaja()
        else: 
            self.Pelaaja2 = Pelaaja.ihmispelaaja()
        self.pelilauta.aseta_kierros(int(tallenne[20]))
        self.pelilauta.selvita_pelatut_ruudut()