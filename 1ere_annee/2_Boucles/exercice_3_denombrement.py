def factorielle ( n ) :
    f = 1
    for i in range ( 1, n+1 ) :
        f = f*i
    return f
    
def denombrement ( p, n ) :
    return int ( factorielle(n) / ( factorielle(p) * factorielle(n-p) ) )
    
print ( factorielle(12) )
print ( denombrement(5,8) )