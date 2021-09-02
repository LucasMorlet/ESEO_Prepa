def puissRec ( a, n ) :
    if ( n == 0 ) :
        return 1
    elif ( n%2 == 0 ) :
        return puissRec ( a, n/2 ) ** 2
    else :
        return a * puissRec ( a, n-1 )
        
        
        
        
for i in range ( 16+1 ) :
    print ( puissRec(2, i), end = " ")