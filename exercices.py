# Exo 2
x = 'abcdefghij'

for i in x:
   print(i)

# Exo 3
age = 18 
print(f"Vous avez {age} ans")
print("Vous avez", age, "ans")

# Exo 4
tortue = "Une tortue"
saute = "saute sur"
chat = "un chat"

print(tortue, saute, chat)
print(f"{tortue} {saute} {chat}")

# Exo 5 
# a = Adrien et b = Ellyne. Il faut inverser pour que a = Ellyne et b = Adrien
a = "Adrien"
b = "Ellyne"

# On créer une variable temporaire pour éviter que a n'écrase b
temp = a 
a = b
b = temp

print(a)
print(b)

# Exo 6 
dict = {'name': 'Marie',
        'age': 27,
        'mange': 'pommes'
        }


# Exo 7
# Stocker ces mots dans une liste

txt= 'il fait beau'

l = txt.split()

# Exo 8 

# Exo 9 
l = [10, 18, 30]
print(l[1])
print(l[2])

# Exo 10 
l = ['a1', 'a2', 'b1','b2', 'a3']
