def somme ( A, B ) :
    # On fait le calcul seulement s'il est mathématiquement possible
    if len(A) == len(B) and len(A[0]) == len(B[0]) :
        # Préparation de la matrice résultat
        C = [0]*len(A)
        for i in range ( len(C) ) :
            C[i] = [0]*len(A[0])
            
        # Calcul
        for i in range ( len(C) ) :
            for j in range ( len(C[0]) ) :
                C[i][j] = A[i][j] + B[i][j]
                
        return C
      
    # Sinon on renvoie une matrice vide 
    else :
        return [0]
        
A = [ [ 1, 2, 3 ], [ 1, 2, 3 ] ]
B = [ [ 1, 0, 1 ], [ 0, 1, 0 ] ]
C = somme ( A, B ) 
for i in range ( len(C) ) :
    print ( C[i] )
print()
    
 
def multiplication ( A, B ) :
    # On fait le calcul seulement s'il est mathématiquement possible
    if len(A[0]) == len(B) :
        # Préparation de la matrice résultat
        C = [0]*len(A)
        for i in range ( len(C) ) :
            C[i] = [0]*len(B[0])
            
        # Calcul
        for i in range ( len(C) ) :
            for j in range ( len(C[0]) ) :
                C[i][j] = 0
                for k in range ( len(A[0]) ) :
                    C[i][j] = C[i][j] + A[i][k] * B[k][j]
                
        return C
      
    # Sinon on renvoie une matrice vide 
    else :
        return [0]
        
A = [ [ 1, 2, 3 ], [ 1, 3, 6 ] ]
B = [ [ 2, 0 ], [ 0, 2 ], [ 1, 1 ] ]
C = multiplication ( A, B ) 
for i in range ( len(C) ) :
    print ( C[i] )