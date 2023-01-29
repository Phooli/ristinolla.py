import Ristinolla

class Main:
        ristinolla = Ristinolla.ristinolla()
        try:
            ristinolla.lataa()
        except Exception: 
           print("Jokin meni pieleen!") 
        ristinolla.pelaa()