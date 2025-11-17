class Calculatrice:

    def mult(x, y):
        return x * y
    
    def addition(x, y):
        return x + y
    
    def power(x, exponent=2):
        return x**exponent
    
    def division(x, y):
        return x / y

class Statistiques:

    def moyenne(liste):
        return sum(liste) / len(liste)
    
    def mediane(liste):
        sorted_list = sorted(liste)
        n = len(sorted_list)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_list[mid - 1] + sorted_list[mid]) / 2
        else:
            return sorted_list[mid]
    
    def variance(liste):
        mean = Statistiques.moyenne(liste)
        return sum((x - mean) ** 2 for x in liste) / len(liste)
  
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

class Animal:
    def __init(self,nom,espece,age):
        self.name = nom
        self.espece = espece
        self.age = age
    def mange(self):
        print(f"(self.name) mange")
    def presenter(self):
        print(f"Je suis {self.nom}, un {self.espece} de {self.age} ans")
    def viellir(self):
        age=age+1
        print(f"{self.nom} a maintenant {self.age} ans")

class Voyante():

    def horoscope(signe):
        if signe == "taureau":
            print(f"Ta journée va bien se passer")
        elif signe == "vierge":
            print("Tu est parfait")
        elif signe == "scorpion":
            print("Tu vas gagner bcp d'argent aujourd'hui")
        elif signe == "gémeaux":
            print("La chance est de ton côté")
        elif signe == "sagittaire":
            print("Attention au verglas")

    def tirer_carte(self):
        cartes = [
            "La Chance Suprême",
            "L’Amour Caché",
            "Le Karma Rapide",
            "L’Argent Mystérieux",
            "La Paresse Absolue",
            "Le Chaos Imminent"
        ]
        print("Ta carte du jour :", random.choice(cartes))
        
class fruit:
    def _init_(self, size, state):
        self.name = pomme
        self.size = size
        self.state = state
    def manger(self):
      print(f"Je mange une {self.name} {state} de {self.size} cm")

class Geometrie:

    def carre(cote):
        return 4 * cote

    def rectangle(longueur, largeur):
        return 2 * (longueur + largeur)

    def triangle(base, hauteur):
        return (base * hauteur) / 2
        
