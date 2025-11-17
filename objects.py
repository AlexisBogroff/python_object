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
  