class Calculatrice:

    def mult(x, y):
        return x * y
    
    def addition(x, y):
        return x + y
    
    def power(x, exponent=2):
        return x**exponent
    
    def division(x, y):
        return x / y

class DistributeurDeBonbons:
    def __init__(self):
        self.nb_bonbons = 10  # On commence avec 10 bonbons

    def donner_bonbon(self):
        if self.nb_bonbons > 0:
            self.nb_bonbons -= 1
            print("🍬 Voici un bonbon !")
        else:
            print("❌ Zut, il n'y a plus de bonbons !")
          
distributeur.donner_bonbon()  # Affiche "🍬 Voici un bonbon !"
