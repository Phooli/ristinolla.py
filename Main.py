import Ristinolla

class Main:
        Ristinolla = Ristinolla.Ristinolla()
        try:
            Ristinolla.lataa()
        except Exception: 
           print("Jokin meni pieleen!") 
        Ristinolla.pelaa()