import Ristinolla

class main:
        ristinolla = Ristinolla.ristinolla()
        try:
            ristinolla.lataa()
        except Exception: 
           print("Jokin meni pieleen!") 
        ristinolla.pelaa()