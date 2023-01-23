import Pelilauta
import Pelaaja

class Ristinolla:
    def __init__(self) -> None:
        self.pelilauta = Pelilauta.Pelilauta()
        self.Pelaaja1 = Pelaaja.ihmisPelaaja()
        #self.tallennus = File("tallennus.txt")

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
                Pelaaja2 = Pelaaja.tietokonePelaaja()
            else: 
                Pelaaja2 = Pelaaja.ihmisPelaaja()

        # Kunnes peli ei ole päättynyt, pelaajat pelaavat vuorotellen meneillään olevan kierroksen(vuoron) perusteella. Tallennetaan peli joka vuoron jälkeen.
        while self.pelilauta.peliLoppu() == False: 
            if self.pelilauta.annaKierros() % 2 == 1: 
                self.Pelaaja1.Pelaa(self.pelilauta)
                #try:
                    #tallenna()
                #except Exception as e:
                    #print("Jokin meni pieleen!")
            if self.pelilauta.peliLoppu() == False: 
                if self.pelilauta.annaKierros() %2 != 1: 
                    Pelaaja2.Pelaa(self.pelilauta)
                    #try: 
                        #tallenna()
                    #except Exception as e:
                        #print("Jokin meni pieleen!")

        # Pelin loputtua tulostetaan lauta, julistetaan lopputulos, ja nollataan pelitilanne sekä keskeneräisen pelin tallennukset. Suljetaan scannerit.
        self.pelilauta.tulostaLauta()
        self.pelilauta.julistaLopputulos()
        self.pelilauta.nollaaPelitilanne()
        #try:  
            #tallenna()
        #except Exception as e:
            #print("Jokin meni pieleen!")

    # Kirjoitetaan pelitilanne-merkkijono tallennus.txt-tiedostoon.
    def tallenna(self):
        tallentaja = FileWriter(tallennus)
        tallentaja.write(Pelilauta.annaPelitilanne())
        tallentaja.close()

    # Ladataan peli, eli luetaan tallennus.txt-tiedosto ja luodaan sen perusteella pelilauta, asetetaan pelaajamäärä, pelaajamäärän perusteella luodaan pelaajat,
    # asetetaan meneillään oleva kierros oikeaksi, ja selvitetään pelatut ruudut taulukkoon, jotta saadaan pelaajilta sopivat syötteet.
    def lataa(self): 
        tallennusPolku = tallennus.toPath()
        luku = Files.readAllLines(tallennusPolku)
        pelilauta = Pelilauta(luku.get(0).charAt(0), luku.get(0).charAt(2), luku.get(0).charAt(4), luku.get(0).charAt(6), luku.get(0).charAt(8), luku.get(0).charAt(10), luku.get(0).charAt(12), luku.get(0).charAt(14), luku.get(0).charAt(16)) 
        pelilauta.asetaPelaajaMaara(Integer.parseInt(luku.get(0).substring(18, 19)))
        if pelilauta.annapelaajaMaara() == 1: 
            Pelaaja2 = tietokonePelaaja()
        else: 
            Pelaaja2 = ihmisPelaaja()
        pelilauta.asetaKierros(Integer.parseInt(luku.get(0).substring(20)))
        pelilauta.selvitaPelatutRuudut()