class Calculatrice:

    def mult(x, y):
        return x * y
    
    def addition(x, y):
        return x + y
    
    def power(x, exponent=2):
        return x**exponent
    
    def division(x, y):
        return x / y

class Recette : 
    def __init__(self, nom, ingredients, etapes) : 
    self.nom = nom
    self.ingredients = ingredients
    self.etapes = etapes
    
    def cuisson(self) :
        print("Chaleur tournante") 
