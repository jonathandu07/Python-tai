# Exercice 1:

# Demande à l'utilisateur de saisir une liste de nombres
liste_nombres = input("Saisissez une liste de nombres : ")

# Convertit la liste de chaines de caractères en liste de nombres
liste_nombres = [int(nombre) for nombre in liste_nombres.split()]

# Calcul de la somme des nombres de la liste
somme = 0
for nombre in liste_nombres:
    somme += nombre
    
# affichage de la somme des nombres de la liste
print("La somme des nombres de la liste est : ", somme)

    
# ******************************** 
print("---------------------------")   
# ******************************** 

# Exercice 2:

# Demande à l'utilisateur de saisir une liste de nombres
liste_nombres = input("Saisissez une liste de nombres : ")

# Convertit la liste de chaines de caractères en liste de nombres
liste_nombres = [int(nombre) for nombre in liste_nombres.split()]

# Initialisation du compteur de nombre pairs
nb_nombre_pairs = 0

# Itère sur la liste de nombres
for nombre in liste_nombres:
    # Verifie si le nombre pair
    if nombre % 2 == 0:
        # Incrémentation du compteur
        nb_nombre_pairs +=1
        
# Affiche le nombre de nombres pairs de la liste
print("Le nombre de nombre pairs de la liste est : ", nb_nombre_pairs)

    
# ******************************** 
print("---------------------------")   
# ******************************** 

# Exercice 3:

# Demande à l'utilisateur de saisir une liste de nombres
liste_nombres = input("Saisissez une liste de nombres : ")

# Convertit la liste de chaines de caractères en liste de nombres
liste_nombres = [int(nombre) for nombre in liste_nombres.split()]

# Tri la liste par ordre croissant
liste_nombres.sort()

# affichage de la liste triée par ordre croissant
print("La liste triée par ordre croissant est : ", liste_nombres)

    
# ******************************** 
print("---------------------------")   
# ******************************** 

# Exercice 4:

# Demande à l'utilisateur de saisir une liste de nombres
liste_nombres = input("Saisissez une liste de nombres : ")

# Convertit la liste de chaines de caractères en liste de nombres
liste_nombres = [int(nombre) for nombre in liste_nombres.split()]

# Inverse la liste
liste_nombres.reverse()

# affichage de la liste inversée
print("La liste inversée est : ", liste_nombres)

    
# ******************************** 
print("---------------------------")   
# ******************************** 

# Exercice 5:

# Demande à l'utilisateur de saisir une liste de nombres
liste_nombres = input("Saisissez une liste de nombres : ")

# Convertit la liste de chaines de caractères en liste de nombres
liste_nombres = [int(nombre) for nombre in liste_nombres.split()]

# Demander à l'utilisateur de saisir le nombre à rechercher
nombre_a_rechercher = int(input("Saisissez le nombre à rechercher : "))

nb_occurrences = 0

# Itère sur la liste de nombres
for nombre in liste_nombres:
    # Vérifie si le nombre est égal au nombre à rechercher
    if nombre == nombre_a_rechercher:
        # Incrémente le compteur
        nb_occurrences +=1
        
# Affiche le nombre d'occurence

print("Le nombre d'occurence est de : ", nb_occurrences)

    
# ******************************** 
print("---------------------------")   
# ******************************** 


# Exercice 7:

# Demande à l'utilisateur de saisir une liste de nombres
liste_nombres = input("Saisissez une liste de nombres : ")

# Convertit la liste de chaines de caractères en liste de nombres
liste_nombres = [int(nombre) for nombre in liste_nombres.split()]

# Demander à l'utilisateur de saisir le nombre à rechercher
valeur_a_rechercher = int(input("Saisissez la valeur à rechercher : "))

# Initialiser les listes des nombres inferieurs à la valeur donnée
liste_nombres_inferieurs = []
liste_nombres_superieurs = []

# Itérer sur la liste nombres

for nombre in liste_nombres:
    # Ajoute le nombre à la liste des nombres inferieurs à la valeur donnée
    if nombre < valeur_a_rechercher:
        liste_nombres_inferieurs.append(nombre)
    else:
        liste_nombres_superieurs.append(nombre)

# Ajoute les nombres supérieurs à la valeur donnée à la fin de la liste de départ
liste_nombre = liste_nombres_inferieurs + liste_nombres_superieurs

# Affichage de la liste avec les nombres supérieurs à la valeur donnée placés en fin de liste
print("La liste avec les nombres supérieurs à la valeur donnée placés en fin de liste est : ", liste_nombre)
