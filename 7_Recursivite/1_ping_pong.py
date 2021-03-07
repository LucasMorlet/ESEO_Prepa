def ping ( n ) :
    print ( "Ping !" )
    if n > 0 :
        pong( n - 1 )
    
def pong ( n ) :
    if n > 0 :
        ping( n - 1 ) 
    print ( "Pong !" )
    
ping( 12 )