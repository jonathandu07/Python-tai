# je créais une variable nomée livre de type string
livre = "Gatsby le Magnifique"

# Je modifie la variable
livre = "Beloved"

# affichage de la variable avec les f-strings
nom = "Doe"
prenom = "Jhon"
age = 25
message = f"Bonjour, je m'appelle {prenom} {nom} et j'ai {age} ans."
print(message)

# Opérations d'arithmétiques

# Addition
resultat_addition = 1 + 2

# Soustraction
resultat_soustraction = 10 - 5

# Multiplication
resultat_multiplication = 3 * 4

# Modulo (reste de la division)
reste_modulo = 10 % 3

# Exposant
exposant = 2 ** 2

# Espacement dans les calculs

# Présentez un espacement pour plus de lisibilité
resultat = 10 * (5 + 3) / 2

# division avec un nombre entier
resultat_division_entier = 10 / 3

# Utilisation de nombre décimaux pour la division
resultat_decimal = 10.0 / 3


# Type de données

# les Integers (les entiers)
age = 25
nombre_articles = 10

# les nombres flottans (les floats)
prix = 19.99
ratio =  3.14

# les chaines de caractères (Strings)
nom = "Alice"
phrase = "Bonjour, comment ça va ?"

# Booléens

est_vrai = True
est_faux = False

# Vérifier le type d'une variable

type_entier = type(42) # type Integer
type_virgule_flottante = type(3.14) # float
type_chaine = type("Python") #str
type_booleen = type(True) # Boolean (bool)


# Exercice variable python
"""
Enoncé :

1- Déclarer trois variables : note_maths, note_physique, note_anglais.
Leur assigner respectivement des valeurs sur 20.
2- Calculer la mouyenne de ces notes et stocker la valeur dans une variable appelée moyenne.
3- Afficher la moyenne avec un message explicite, par exemple : la moyenne est de [Valeur de la moyenne].
4- Supposons que l'étudiant ait reçu une note supplémentaire de 2 points en mathématique. Mettre à jour
la variable note_maths.
5- Calculer la moyenne.
6- Afficher la nouvelle moyenne avec un message approprié.
"""

# Déclaration des notes (des variables)
note_maths = 13
note_anglais = 16
note_physique = 18

# calculer la moyenne (déclaration de la variable moyenne)
moyenne = (note_maths + note_anglais + note_physique) / 3

# affichage de la moyenne initiale
print("La moyenne des notes est :", moyenne)

# mise à jour de la note de mathématiques
note_maths +=2

# Recalcul de la moyenne avec la nouvelle note de mathématiques
moyenne = (note_maths + note_anglais + note_physique) / 3

# affichage de la nouvelle moyenne
print("Après mise à jour, la nouvelle moyenne est des : ", moyenne)

