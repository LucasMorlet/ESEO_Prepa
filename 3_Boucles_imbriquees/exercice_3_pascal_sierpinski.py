def factorielle ( n ) :
    f = 1
    for i in range ( 1, n+1 ) :
        f = f*i
    return f
    
def denombrement ( p, n ) :
    return int ( factorielle(n) / ( factorielle(p) * factorielle(n-p) ) )
    
def pascal ( max_size ) :
    for i in range ( 0, max_size + 1 ) :
        for j in range ( 0, i+1 ) :
            print ( denombrement( j, i ), end=" " )
        print ()
        
def sierpinski ( max_size ) :
    for i in range ( 0, max_size + 1 ) :
        for j in range ( 0, i+1 ) :
            if ( denombrement( j, i ) % 2 ) :
                print ( "X", end="" )
            else :
                print ( " ", end="" )
        print ()
    
pascal ( 10 )
print ( "" )
sierpinski(31)