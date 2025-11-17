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
