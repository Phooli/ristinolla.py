import random

class Pelaaja: 
       def __init__(self):
            pass
       def Pelaa(self):
            pass 
        
class ihmisPelaaja(Pelaaja):

    # Tulostetaan pelilauta.
    # Tarkistetaan ihmispelaajien määrä, kysytään meneillään olevan vuoron perusteella oikealta pelaajalta ruudun numeroa. 
    # Varmistetaan, että numero vastaa ruutua, että ruutu ei ole täytetty, ja että ylipäätään syötetään numero. 
    # Asetetaan pelaajan merkki ja päivitetään pelitilanne.
    def Pelaa(self, Pelilauta):
        syoteSallittu = False
        Pelilauta.tulostaLauta()
        while syoteSallittu == False:
            try:
                if Pelilauta.annapelaajaMaara() == 2:
                    if Pelilauta.annaKierros() %2 != 0: 
                        seuraavaRuutu = int(input("Pelaaja 1 (X): Aseta merkkisi vapaaseen ruutuun syöttämällä ruudun numero: "))   
                    else:
                        seuraavaRuutu= int(input("Pelaaja 2 (O): Aseta merkkisi vapaaseen ruutuun syöttämällä ruudun numero: "))
                else:
                    seuraavaRuutu = int(input("Aseta merkkisi vapaaseen ruutuun syöttämällä ruudun numero: "))
                if seuraavaRuutu > 9 or seuraavaRuutu < 1:
                    print("Numero ei vastaa ruutua.\n")
                    continue
                if seuraavaRuutu in Pelilauta.annaPelatutRuudut():
                    print("Ruutu on jo täytetty.\n")
                    continue
                syoteSallittu = True
                Pelilauta.asetaMerkki(seuraavaRuutu)
                Pelilauta.paivitaPelitilanne()
            except ValueError: 
                print("Syötteesi ei ole sopiva numero.\n")

class tietokonePelaaja(Pelaaja):
    
    # Tulostetaan pelilauta.
    # Generoidaan satunnaisluku 1-9, kunnes luku vastaa vapaan ruudun numeroa. 
    # Asetetaan merkki vapaaseen ruutuun.
    # Päivitetään pelitilanne.
    def Pelaa(self, Pelilauta):
        Pelilauta.tulostaLauta()
        print("Tietokonepelaaja asettaa merkin...")
        #try:
        #   Thread.sleep(3000);
        #except Exception as e:
        #    Thread.currentThread().interrupt()
        seuraavaRuutu = random.randint(1, 9)
        while seuraavaRuutu in Pelilauta.annaPelatutRuudut():
            seuraavaRuutu = random.randint(1, 9)
        Pelilauta.asetaMerkki(seuraavaRuutu)
        Pelilauta.paivitaPelitilanne()