class Calculatrice:

    def mult(x, y):
        return x * y
    
    def addition(x, y):
        return x + y
    
    def power(x, exponent=2):
        return x**exponent
    
    def division(x, y):
        return x / y
    
class Geometrie:

    def carre(cote):
        return 4 * cote

    def rectangle(longueur, largeur):
        return 2 * (longueur + largeur)

    def triangle(base, hauteur):
        return (base * hauteur) / 2