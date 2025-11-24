# exercice 1
# def entree_autorisee(age):
#     if age >= 18:
#         return True
#     else:
#         return False

# print(entree_autorisee(20))


# exercice 2
# # x = "avbrpeobnrg"
# # for i in x:
# #     # print(i)


# # exercice 3
# age = 18
# print(f"Vous avez {age} ans.")


# exercice 4
# tortue = "une tortue"
# saute = "saute sur"
# chat = "un chat"

# print(f"{tortue} {saute} {chat}.")


# exercice 5
# a = 5
# b = 10
# temp = None

# print("Before swapping:")
# print("a :", a)
# print("b :", b)

# temp = a 
# a = b
# b = temp

# print("After swapping:")
# print("a :", a)
# print("b :", b)


# exercice 6
# dico = {
#     "nom": "Marie",
#     "âge": 27,
#     "fruit": "pomme"
# }

# nom = dico["nom"]
# age = dico["âge"]
# fruit = dico["fruit"]

# print(f"Une personne qui s'appelle {nom} et qui a {age} ans et mange des {fruit}s.")


# exercice 7
# text = "il fait beau"
# l = []
# mots = text.split()
# for mot in mots:
#     l.append(mot)
# print(l)


# exercice 8
# l = ["a", "b", "c", "d"]

# for key, value in enumerate(l):
#     print(f"{value}{key}")


# exercice 9
# l = [10, 18, 30]
# for i in l:
#     if i % 6 == 0:
#         print(f"{i}")


# exercice 10
# l = ['a1', 'a2', 'b1', 'b2', 'a3']
# for i in l:
#     # if i in ['a1', 'a2', 'a3']:
#     #     print(i)
#     if i == 'a1' or i == 'a2' or i == 'a3':
#         print(i)


# exercice 11
# def renvoyer_chaine_caracteres(l):
#         return " ".join(l)

# x = renvoyer_chaine_caracteres(['coucou', 'je', 'suis', 'une', 'tortue'])
# print(x)


# exercice 12
# def tshirt_sizes(taille):
#     count_S = 0
#     count_M = 0
#     count_L = 0

#     for i in taille:
#         if i == 'S':
#             count_S += 1
#         elif i == 'M':
#             count_M += 1
#         elif i == 'L':
#             count_L += 1

#     return {'S': count_S, 'M': count_M, 'L': count_L}

# taille = ['S', 'S', 'M', 'S', 'L', 'S', 'M']

# print(tshirt_sizes(taille))