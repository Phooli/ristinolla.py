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
                if pelilauta.pelaajamaara == 2:
                    if pelilauta.kierros %2 != 0: 
                        seuraava_ruutu = int(input("Pelaaja 1 (X): Aseta merkkisi vapaaseen ruutuun syöttämällä ruudun numero: "))   
                    else:
                        seuraava_ruutu= int(input("Pelaaja 2 (O): Aseta merkkisi vapaaseen ruutuun syöttämällä ruudun numero: "))
                else:
                    seuraava_ruutu = int(input("Aseta merkkisi vapaaseen ruutuun syöttämällä ruudun numero: "))
                if seuraava_ruutu > 9 or seuraava_ruutu < 1:
                    print("Numero ei vastaa ruutua.\n")
                    continue
                if seuraava_ruutu in pelilauta.pelatut_ruudut:
                    print("Ruutu on jo täytetty.\n")
                    continue
                syote_sallittu = True
                pelilauta.aseta_merkki(seuraava_ruutu)
                pelilauta.paivita_pelitilanne()
            except ValueError: 
                print("Syötteesi ei ole sopiva numero.\n")

class tietokonepelaaja(pelaaja):
    
    # 1. Tulostetaan pelilauta.
    # 2. Jos löytyy yksi ruutu, jolla voitetaan tai voidaan estää vastustajan voitto, pelataan se.
    # Muussa tapauksessa pelataan prioriteetein: 1. keskimmäinen ruutu 2. satunnainen kulma 3. muu ruutu.
    # 3. Asetetaan merkki vapaaseen ruutuun.
    # 4. Päivitetään pelitilanne.
    def pelaa(self, pelilauta):
        pelilauta.tulosta_lauta()
        print("Tietokonepelaaja asettaa merkin...")
        time.sleep(3)
        seuraava_ruutu = pelilauta.selvita_voittava_ruutu()
        if (seuraava_ruutu > 0):
            pelilauta.aseta_merkki(seuraava_ruutu)
        elif (5 not in pelilauta.pelatut_ruudut):
            pelilauta.aseta_merkki(5)
        elif (1 not in pelilauta.pelatut_ruudut
            or 3 not in pelilauta.pelatut_ruudut
            or 7 not in pelilauta.pelatut_ruudut
            or 9 not in pelilauta.pelatut_ruudut):
                seuraava_ruutu = random.choice([1,3,7,9])
                while seuraava_ruutu in pelilauta.pelatut_ruudut:
                    seuraava_ruutu = random.choice([1,3,7,9])
                pelilauta.aseta_merkki(seuraava_ruutu)
        else:
            seuraava_ruutu = random.choice([2,4,6,8])
            while seuraava_ruutu in pelilauta.pelatut_ruudut:
                seuraava_ruutu = random.choice([2,4,6,8])
            pelilauta.aseta_merkki(seuraava_ruutu)
        pelilauta.paivita_pelitilanne()