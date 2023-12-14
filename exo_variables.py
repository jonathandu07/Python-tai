# Exercice 1:

# Demande à l'utilisateur de saisir son nom
nom = input("Quel est votre nom\n")

# Demande de l'age de l'utilisateur
age = int(input("Quel age avez-vous ?\n"))

# afficher le message
print("Bonjour, {} : Vous avez {} ans.".format(nom, age))

# Exercice 2:

# Demande à l'utilisateur de saisir le premier nombre
nombre1 = int(input("Saisissez le premier nombre : "))

# Demande à l'utilisateur de saisir le second nombre
nombre2 = int(input("Saisissez le second nombre : "))

# Calcule la somme !
somme = nombre1 + nombre2

# Calcule la difference !
difference = nombre1 - nombre2

# Calcule le produit !
produit = nombre1 * nombre2

# Calcule le quotient !
quotient = nombre1 / nombre2

# afficher les résultats
print(f"La somme des deux nombres est : {somme}")
print("La différence des deux nombres est : ",difference)
print("Le produit des deux nombres est : ",produit)
print("Le quotient des deux nombres est : ",quotient)

# Exercice 3:

# Dictionnaire contenant les noms des nombres en lettres
dict_nombres = {
    1:"un",
    2:"deux",
    3:"trois",
    4:"quatre",
    5:"cinq",
    6:"six",
    7:"sept",
    8:"huit",
    9:"neuf",
    10:"dix",
}

# demande à l'utilisateur de rentrer un nombre
nombre = int(input("Saisissez un nombre : "))

# afficher le nombre en lettres
print(dict_nombres[nombre])

# Autres solution pour l'exercice 3

# Dictionnaire contenant les noms en dizaine
dict_dizaine = {
    1:"dix",
    2:"vingt",
    3:"trente",
    4:"quarante",
    5:"cinquante",
    6:"soixante",
    7:"soixante-dix",
    8:"quatre-vingt",
    9:"quatre-vingt-dix"
}

# Dictionnaire contenant les noms des unités
dict_unite = {
    1:"un",
    2:"deux",
    3:"trois",
    4:"quatre",
    5:"cinq",
    6:"six",
    7:"sept",
    8:"huit",
    9:"neuf"
}

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Saisissez un nombre : \n"))

# calcule la dizaine !
# // = division entière qui signifie : 70 // 10 = 7
dizaine = nombre // 10

# Calcule l'unité
unite = nombre % 10

# affiche le nombre en lettres
print(dict_dizaine[dizaine] + "-" + dict_unite[unite])

# Exercice 4:

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Saisissez un nombre : "))

# Inversion du nombre
nombre_inverse = 0 #Initialisation du nombre inversé à zero
while nombre > 0: #Tant que le nombre original est supérieur à zéro
    nombre_inverse = nombre_inverse * 10 + nombre % 10 #Inversion du nombre en ajoutant le dernier chiffre
    nombre //= 10 # Suppression du dernier chiffre du nombre original
    
# afficher le nombre inversé
print(nombre_inverse)

# Autre solution (beaucoup plus simple)

# On demande le nombre à l'utilisateur
nombre = int(input("Saissez le nombre : "))

# Inversion du nombre
nombre_inverse = 0 #Initialisation du nombre inversé à zero

for chiffre in reversed(str(nombre)): # Pour chaque chiffre dans le nombre, en partant de la fin
    nombre_inverse = nombre_inverse * 10 + int(chiffre) # Inversion du nombre en ajoutant chaque chiffre
    
# Afficher le nombre inverse
print(nombre_inverse)

# Exercice 5:

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Saissez le nombre : "))

# Determine le type du nombre !
if nombre > 0: # Si le nombre est positif
    type_nombre = "Positif"
elif nombre < 0: # Si le nombre est négatif
    type_nombre = "Négatif"
else: # Si le nombre est nul
    type_nombre = "Nul"

# Affiche le type du nombre
print("Le nombre est {}".format(type_nombre))

# autre solution plus simple 

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Saissez le nombre : "))

if abs(nombre) > 0: #Si la valeur absolue du nombre est supérieur à 0
    type_nombre = "Positif" if nombre > 0 else "Négatif" # Utilisation d'une expression conditionnelle pour déterminer le type
else:
    type_nombre = "Nul"
    

# Affiche le type du nombre
print("Le nombre est {}".format(type_nombre))