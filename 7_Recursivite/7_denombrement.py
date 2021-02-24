def denombrementRec ( p, n ) :
    if p < 0 : 
        return 0
    if n < 0 : 
        return 0
    if p > n : 
        return 0
    if p == 0 and n == 0 : 
        return 1
        
    return denombrementRec ( p-1, n-1 ) + denombrementRec ( p, n-1 )
    
    
for n in range ( -10, 10 ) :
    for p in range ( -10, 10 ) :
        res = denombrementRec ( p, n )
        if res > 0 :
            print ( denombrementRec ( p, n ), end = " " )
    print()