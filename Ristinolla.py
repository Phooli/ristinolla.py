import Pelilauta
import Pelaaja

class Ristinolla:
    def __init__(self, Pelaaja2 = Pelaaja):
        self.pelilauta = Pelilauta.Pelilauta('1','2','3','4','5','6','7','8','9',)
        self.Pelaaja1 = Pelaaja.ihmisPelaaja()
        self.Pelaaja2 = Pelaaja2

    def pelaa(self):
        if self.pelilauta.annaKierros() != 1: 
            jatketaankoTallennuksesta = input("Haluatko jatkaa tallennettua peliä? (Syötä K/E): ")
            if jatketaankoTallennuksesta == 'K' or jatketaankoTallennuksesta == 'k': 
                print("Jatketaan tallennettua peliä...")
                #try: 
                #    Thread.sleep(3000)
                #except Exception as e:
                #    Thread.currentThread().interrupt()
            else: 
                self.pelilauta.nollaaPelitilanne()

        # Jos pelaajamäärää ei asetettu, kysytään ihmispelaajien määrää. 1 = Pelaaja 2 on tietokonepelaaja. 2 = Pelaaja 2 on toinen ihmispelaaja.
        while self.pelilauta.annapelaajaMaara() != 1 and self.pelilauta.annapelaajaMaara() != 2: 
            try: 
                self.pelilauta.asetaPelaajaMaara(int(input("Syötä ihmispelaajien määrä (1/2) ")))
                if self.pelilauta.annapelaajaMaara() < 1 or self.pelilauta.annapelaajaMaara() > 2: 
                    print("Syötetty pelaajamäärä ei kelpaa.\n")
                    continue
            except ValueError:
                print("Syötteesi ei ole sopiva numero.\n")
            if self.pelilauta.annapelaajaMaara() == 1: 
                self.Pelaaja2 = Pelaaja.tietokonePelaaja()
            else: 
                self.Pelaaja2 = Pelaaja.ihmisPelaaja()

        # Kunnes peli ei ole päättynyt, pelaajat pelaavat vuorotellen meneillään olevan kierroksen(vuoron) perusteella. Tallennetaan peli joka vuoron jälkeen.
        while self.pelilauta.peliLoppu() == False: 
            if self.pelilauta.annaKierros() % 2 == 1: 
                self.Pelaaja1.Pelaa(self.pelilauta)
                try:
                    self.tallenna()
                except Exception:
                    print("Jokin meni pieleen!")
            if self.pelilauta.peliLoppu() == False: 
                if self.pelilauta.annaKierros() %2 != 1: 
                    self.Pelaaja2.Pelaa(self.pelilauta)
                    try: 
                        self.tallenna()
                    except Exception:
                        print("Jokin meni pieleen!")

        # Pelin loputtua tulostetaan lauta, julistetaan lopputulos, ja nollataan pelitilanne sekä keskeneräisen pelin tallennukset. Suljetaan scannerit.
        self.pelilauta.tulostaLauta()
        self.pelilauta.julistaLopputulos()
        self.pelilauta.nollaaPelitilanne()
        try:  
            self.tallenna()
        except Exception:
            print("Jokin meni pieleen!")

    # Kirjoitetaan pelitilanne-merkkijono tallennus.txt-tiedostoon.
    def tallenna(self):
        tallennus = open("tallennus2.txt", "w")
        tallennus.write(self.pelilauta.annaPelitilanne())
        tallennus.close()

    # Ladataan peli, eli luetaan tallennus.txt-tiedosto ja luodaan sen perusteella pelilauta, asetetaan pelaajamäärä, pelaajamäärän perusteella luodaan pelaajat,
    # asetetaan meneillään oleva kierros oikeaksi, ja selvitetään pelatut ruudut taulukkoon, jotta saadaan pelaajilta sopivat syötteet.
    def lataa(self): 
        tallennus = open("tallennus2.txt", "r")
        tallenne = tallennus.read()
        tallennus.close()
        self.pelilauta = Pelilauta.Pelilauta(tallenne[0], tallenne[2], tallenne[4], tallenne[6], tallenne[8], tallenne[10], tallenne[12], tallenne[14], tallenne[16]) 
        self.pelilauta.asetaPelaajaMaara(int(tallenne[18]))
        if self.pelilauta.annapelaajaMaara() == 1: 
            self.Pelaaja2 = Pelaaja.tietokonePelaaja()
        else: 
            self.Pelaaja2 = Pelaaja.ihmisPelaaja()
        self.pelilauta.asetaKierros(int(tallenne[20]))
        self.pelilauta.selvitaPelatutRuudut()