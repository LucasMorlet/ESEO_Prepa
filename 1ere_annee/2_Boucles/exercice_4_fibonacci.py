def fibonacci ( n ) :
    # Pour rappel, u0 = 0 et u1 = 1
    if n == 0 or n == 1 :
        return n
    
    # On définit les valeurs de départ : 0 et 1
    a = 0
    b = 1
    
    # A chaque tour de boucle on fait la somme de a et b, puis un décalage de variable
    for i in range ( 2, n+1 ) :
        r = a+b
        a = b
        b = r
        
    return b 

# On appelle la fonction dans une boucle pour vérifier si tout est bon    
for i in range ( 20 ) :
    print ( fibonacci ( i ), end = ", " )