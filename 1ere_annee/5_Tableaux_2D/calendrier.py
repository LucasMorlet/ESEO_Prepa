# Création d'un tableau à deux dimensions
# Remplissage bi-dimensionnel d'un tableau 2D
# Remplissage uni-dimensionnel d'un tableau 2D
# Recherche bi-dimensionnelle et exhaustive dans un tableau 2D
# Affichage ligne par ligne d'un tableau 2D

def calendrier ( jour_1, nb_jours ) :
    # a) Création du tableau
    tab = [0]*6
    for i in range ( len(tab) ) :
        tab[i] = [0]*7
        
    # b) Remplissage du tableau avec les jours de la semaine
    semaine = [ "L", "M", "M", "J", "V", "S", "D" ];
    for i in range ( len(tab) ) :
        for j in range ( len(tab[i]) ) :
            tab[i][j] = semaine[j]
    
    # d) Remplissage du tableau avec la date du jour
    jour = jour_1
    ligne = 0
    for i in range ( 1, nb_jours + 1 ) :
        tab[ligne][jour] = i
        jour = jour + 1
        if jour >= 7 :
            jour = 0
            ligne = ligne + 1
            
    return tab
    
# c) Affichage ligne par ligne du tableau  
def affichage_mois ( nom, tab ) :
    print ( "*****", nom, "*****" )
    for i in range ( len(tab) ) :
        print ( tab[i] )
    print()

# e) Transformation de certains jours en jour férié    
def jour_ferie ( jour, tab, caractere ) :
    for i in range ( len(tab) ) :
        for j in range ( len(tab[i]) ) :
            if tab[i][j] == jour :
                tab[i][j] = caractere
    
octobre = calendrier ( 3, 31 )
novembre = calendrier ( 6, 30 )
decembre = calendrier ( 1, 31 )  

jour_ferie (  1, novembre, "T" ) # Toussaint
jour_ferie ( 11, novembre, "A" ) # Armistice
jour_ferie ( 25, decembre, "N" ) # Noël

print()
affichage_mois ( "Octobre", octobre )
affichage_mois ( "Novembre", novembre )
affichage_mois ( "Décembre", decembre )
print()

