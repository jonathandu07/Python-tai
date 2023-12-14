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

