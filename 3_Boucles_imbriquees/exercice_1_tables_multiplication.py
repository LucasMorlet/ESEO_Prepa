def tables_multiplication ( m, n ) :
    for i in range ( 1, m+1 ) :
        for j in range ( 1, n+1 ) :
            print ( i*j, end = " " )
        print ( "" )
        
tables_multiplication ( 5, 9 )