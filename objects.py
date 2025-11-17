class Calculatrice:

    def mult(x, y):
        return x * y
    
    def addition(x, y):
        return x + y
    
    def power(x, exponent=2):
        return x**exponent
    
    def division(x, y):
        return x / y


class Chaussure:

    def _init_(self, nom):
        self.brand = Adidas
        self.gender = Femme
        self.model = Sambas
        self.color = marron
        self.size = 39 
        self.name = Sabera
    
    def appartenance(self):
        print(f"Je cherche des {self.brand} {self.model} en {self.color} pour {self.gender}, je fais du {self.size}.")

    
