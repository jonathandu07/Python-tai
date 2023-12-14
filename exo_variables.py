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
nombre = int(input("Saisissez le nombre : "))

# Inversion du nombre
nombre_inverse = 0 #Initialisation du nombre inversé à zero

for chiffre in reversed(str(nombre)): # Pour chaque chiffre dans le nombre, en partant de la fin
    nombre_inverse = nombre_inverse * 10 + int(chiffre) # Inversion du nombre en ajoutant chaque chiffre
    
# Afficher le nombre inverse
print(nombre_inverse)

# Exercice 5:

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Saisissez le nombre : "))

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
nombre = int(input("Saisissez le nombre : "))

if abs(nombre) > 0: #Si la valeur absolue du nombre est supérieur à 0
    type_nombre = "Positif" if nombre > 0 else "Négatif" # Utilisation d'une expression conditionnelle pour déterminer le type
else:
    type_nombre = "Nul"
    

# Affiche le type du nombre
print("Le nombre est {}".format(type_nombre))

# Exercice 6:

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Saisissez le nombre : "))

# Détermine le type du nombre
# Vérifie si le reste de la division du nombre par 2 est égal à 0
# Si c'est le cas, le nombre est pair, sinon il est impair
if nombre % 2 == 0:
    type_nombre = "pair"
else:
    type_nombre = "impair"
    
# Affiche le type du nombre
print("Le nombre est {}".format(type_nombre))

# Méthode plus simple ou seconde solution ou otra solucion, other solution

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Saisissez le nombre : "))

# Déternime le type du nombre
# Utilise la fonction divmod qui renvoie à la fois le quotient et le reste de la division de nombre par 2

quotient, reste = divmod(nombre, 2)

# Vérifie si le reste de la division par 2 est égal à zéro
# SI c'est le cas, le nombre est pair, sinon il est impair
if reste == 0:
    type_nombre = "pair"
else:
    type_nombre = "impair"
    
# Affiche le type du nombre
print("Le nombre est {}.".format(type_nombre))

# Exercice 7:

# Définition des deux premier nombres de la séquence de Fibonacci
a = 0
b = 1

# Demande à l'utilisateur de saisir un nombre
n = int(input("Saisissez un nombre : "))

# Calcul dunombre suivant dans la séquence
# La boucle for itère de 0 à n-1 pour calculer le nombre suivant dans la séquence
for i in range(n - 1):
    # La valeur de a devient la valeur de b, et la valeur de b devient la somme des anciennes valeurs de a et de b
    a, b = b, a + b
    
# Affichage du nombre suivant
print("Le nombre suivant dans la séquence de Fibonacci est :", b)


# Exercice 8:

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Saisissez le nombre : "))

# Affiche la table de multiplication
for i in range(1, 11):
    print(nombre, "X", i, "=", nombre *1)
    
# Une autre solution

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Saisissez le nombre : "))

i = 1

# Affiche la table de multiplication
while i <= 10:
    print(nombre, "X", i, "=", nombre * i)
    
# Exercice 9

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Saisissez le nombre : "))

# Initialise le nombre de diviseurs
nb_diviseurs = 0

# Itère sur les nombres de 1 jusqu'à nombre
for i in range(1, nombre + 1):
    # Vérifie si i est un diviseur de nombre
    if nombre % i == 0:
        # Increment le nombre de diviseursd
        nb_diviseurs += 1
        
# Affiche le nombre de diviseurs
print("LE nombre de diviseurs de", nombre, "est : ", nb_diviseurs)


# Autre solution
import math

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Saisissez le nombre : "))

# Initialise le nombre de diviseurs
nb_diviseurs = 0

# Récupère les facteurs du nombre
facteurs = math.factor(nombre)

# compte le nombre de facteurs
for facteur in facteurs:
    nb_diviseurs += 1
    
# Affiche le nombre de diviseurs
print("LE nombre de diviseurs de", nombre, "est : ", nb_diviseurs)


# Exercice 10 :

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Saisissez le nombre : "))

# Initialise le plus grand diviseur
plus_grand_diviseur = 1

# Itère sur les nombres de 1 à nombre
for i in range(1, nombre + 1):
    # Vérifie si i est un diviseur de nombre
    if nombre % i == 0:
        # Met à jour le plus grand diviseur
        if i > plus_grand_diviseur:
            plus_grand_diviseur = i
            
# Affiche le plus grand diviseur
print("Le plus grand diviseur de", nombre, "est : ", plus_grand_diviseur)

# Autre solution

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Saisissez le nombre : "))

# Récupère le plus grand diviseur
plus_grand_diviseur = math.gcd(nombre, nombre)

# Affiche le plus grand diviseur
print("Le plus grand diviseur de", nombre, "est : ", plus_grand_diviseur)

# Exercice final sur les variables : Calcul de la moyenne

# 
