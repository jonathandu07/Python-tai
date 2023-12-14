# Les listes en Python

reseaux_sociaux = ["Facebook", "Twitter", "Google", "Tiktok", "Snapchat"]
# len permet de compter le nombre d'éléments dans une liste
print(len(reseaux_sociaux))
    
# ******************************** 
print("---------------------------")   
# ******************************** 


# Ajouter un élément à une liste
liste = []
liste.append("Facebook")
for i in liste:
    print(i) 
    
# ******************************** 
print("---------------------------")   
# ******************************** 


# Supprimer une entrée par index:
del liste[0]
# Je vérifie si ma liste est vide
if len(liste) == 0:
    print("La liste est vide")
    
# ******************************** 
print("---------------------------")   
# ******************************** 

    
# Supprimer une entrée par valeur:
reseaux_sociaux.remove("Tiktok")
# Je vérifie si Tiktok est bel et bien supprimé
for i in reseaux_sociaux:
    print(i) 
    
# ******************************** 
print("---------------------------")   
# ******************************** 

# Inverser les valeurs d'une liste:
reseaux_sociaux.reverse()
# Je vérifie que ma liste est bien inversée
for i in reseaux_sociaux:
    print(i) 
    
    
# ******************************** 
print("---------------------------")   
# ******************************** 


# Compter le nombre d'élément d'une liste

nombre_d_items = len(reseaux_sociaux)

# J'affiche le nombre d'élément dans ma liste
print("La longueur de ma liste est de : ", nombre_d_items)

    
# ******************************** 
print("---------------------------")   
# ******************************** 

# Trouver l'index d'une valeur dans une liste
# L'index signifie la position dans la liste

index_de_facebook = reseaux_sociaux.index("Facebook")

# On affiche l'index souhaité
print("L'index souhaité : ", index_de_facebook)

    
# ******************************** 
print("---------------------------")   
# ******************************** 

# Copier une liste

x = [1, 2, 3]
# [:] permet de copier une liste
y = x[:]

# On affiche la liste y pour vérifier si c'est bel et bien une copie de la liste x

for i in y:
    print(i)
    
    
# ******************************** 
print("---------------------------")   
# ******************************** 

# Tri des éléments d'une liste
# La méthode (la fonction) sort() trie les éléments de la liste. Pour les listes de chaînes de caractères, le trie est alphabétique, et pour les nombres, le tri est numérique.

reseaux_sociaux.sort()
print(reseaux_sociaux)