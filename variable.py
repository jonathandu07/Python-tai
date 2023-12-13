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

# Exercises les types de données en Python
"""
Enoncé :
1. Déclarez une variable entier et attribuez-lui une valeur entière de votre choix.
2. Déclarez une variable decimal et attribuez-lui une valeur décimale (nombre à
virgule) de votre choix.
3. Déclarez une variable texte et attribuez-lui une chaîne de caractères (texte) de
votre choix.
4. Déclarez une variable vrai_ou_faux et attribuez-lui une valeur booléenne (True
ou False) en fonction d'une affirmation de votre choix.
5. Affichez le type de chaque variable en utilisant la fonction type().
6. Effectuez une opération mathématique en utilisant la variable entier et la variable
decimal, puis affichez le résultat.
7. Concaténez la variable texte avec une autre chaîne de caractères de votre choix,
puis affichez le résultat.
8. Inversez la valeur de la variable vrai_ou_faux (si elle est True, elle devient
False, et vice versa) et affichez la nouvelle valeur.
"""

# déclaration de la variables
entier = 42
decimal = 3.14
texte = "Bonjour, "
vrai_ou_faux = True

# Affichage des types
print("Type entier :", type(entier))
print("Type décimal :", type(decimal))
print("Type texte :", type(texte))
print("Type vrai_ou_faux :",type(vrai_ou_faux))

# Opération mathématique
resultat_operation = entier + decimal
print("Résultat de l'opération mathématique :", resultat_operation)
# concaténation de chaines de caractères
nouveau_texte = texte + "Comment ça va ?"
print("Nouvelle chaine de caractères :", nouveau_texte)

# Inversion de la valeur booléenne
vrai_ou_faux = not vrai_ou_faux
print("Nouvelle valeur de vrai ou de faux:", vrai_ou_faux)