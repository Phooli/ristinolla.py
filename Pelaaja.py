import random
import time

class pelaaja: 
       def __init__(self):
            pass
       def pelaa(self):
            pass 
        
class ihmispelaaja(pelaaja):

    # Tulostetaan pelilauta.
    # Tarkistetaan ihmispelaajien määrä, kysytään meneillään olevan vuoron perusteella oikealta pelaajalta ruudun numeroa. 
    # Varmistetaan, että numero vastaa ruutua, että ruutu ei ole täytetty, ja että ylipäätään syötetään numero. 
    # Asetetaan pelaajan merkki ja päivitetään pelitilanne.
    def pelaa(self, pelilauta):
        syote_sallittu = False
        pelilauta.tulosta_lauta()
        while syote_sallittu == False:
            try:
                if pelilauta.anna_pelaajamaara() == 2:
                    if pelilauta.anna_kierros() %2 != 0: 
                        seuraava_ruutu = int(input("Pelaaja 1 (X): Aseta merkkisi vapaaseen ruutuun syöttämällä ruudun numero: "))   
                    else:
                        seuraava_ruutu= int(input("Pelaaja 2 (O): Aseta merkkisi vapaaseen ruutuun syöttämällä ruudun numero: "))
                else:
                    seuraava_ruutu = int(input("Aseta merkkisi vapaaseen ruutuun syöttämällä ruudun numero: "))
                if seuraava_ruutu > 9 or seuraava_ruutu < 1:
                    print("Numero ei vastaa ruutua.\n")
                    continue
                if seuraava_ruutu in pelilauta.anna_pelatut_ruudut():
                    print("Ruutu on jo täytetty.\n")
                    continue
                syote_sallittu = True
                pelilauta.aseta_merkki(seuraava_ruutu)
                pelilauta.paivita_pelitilanne()
            except ValueError: 
                print("Syötteesi ei ole sopiva numero.\n")

class tietokonepelaaja(pelaaja):
    
    # Tulostetaan pelilauta.
    # Generoidaan satunnaisluku 1-9, kunnes luku vastaa vapaan ruudun numeroa. 
    # Asetetaan merkki vapaaseen ruutuun.
    # Päivitetään pelitilanne.
    def pelaa(self, pelilauta):
        pelilauta.tulosta_lauta()
        print("Tietokonepelaaja asettaa merkin...")
        try: 
            time.sleep(3)
        except Exception:
            print("Jokin meni pieleen!")
        seuraava_ruutu = random.randint(1, 9)
        while seuraava_ruutu in pelilauta.anna_pelatut_ruudut():
            seuraava_ruutu = random.randint(1, 9)
        pelilauta.aseta_merkki(seuraava_ruutu)
        pelilauta.paivita_pelitilanne()