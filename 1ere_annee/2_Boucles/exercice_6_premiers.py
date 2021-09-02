from math import sqrt

# Test de primalité
def est_premier ( n ) :
    # 0 et 1 ne sont pas premiers
    if ( n == 0 or n == 1 ) :
        return False
        
    # On teste tous les nombres i jusqu'à la racine de n
    fin = int(sqrt(n)) + 1
    for i in range ( 2, fin ) :
        # Si i est un diviseur de n, alors n n'est pas premier
        if n%i == 0 :
            return False
    # Si on a pas trouvé de diviseur avant la racine de n, c'est que n est premier
    return True
 
# Les nombres premiers inférieurs à 100 
for i in range ( 100 ) :
    if est_premier ( i ) :
        print ( i, end = ", " )
print ( "" )
        
# Plus petit diviseur
def plus_petit_diviseur ( n ) :
    # Le plus petit diviseur de 0 est par convention 1
    if ( n == 0 or n == 1 ) :
        return 1
        
    fin = int(sqrt(n)) + 1
    for i in range ( 2, fin ) :
        if n%i == 0 :
            return i
    
    # Si on a pas trouvé de diviseur, le nombre est premier et il est son propre plus petit diviseur
    return n
    
def decoupage_premiers ( n ) :
    print ( n, end = " = " )
    # Tant que le nombre est supérieur à 1
    while n > 1 :
        # On calcule son plus petit diviseur
        ppd = plus_petit_diviseur ( n )
        print ( ppd, end = "" )
        # Affichage uniquement : si on a pas encore fini, on ajoute un 'x'
        if ppd != n :
            print ( " x ", end = "" )
        # Puis on divise le nombre par son plus petit diviseur        
        n = int (n / ppd)

decoupage_premiers ( 96900 )