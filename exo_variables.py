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