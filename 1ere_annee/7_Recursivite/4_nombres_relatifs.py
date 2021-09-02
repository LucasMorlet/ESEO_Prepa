def nombresRelatifs ( n ) :
    print ( -n, end=" " )
    if ( n > 0 ) :
        nombresRelatifs ( n - 1 )
        print ( n, end=" " )
        
nombresRelatifs ( 5 )