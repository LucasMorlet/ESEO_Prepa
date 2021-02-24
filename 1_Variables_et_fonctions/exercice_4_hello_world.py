def hello_world ( langue ) :
    if langue == "fr" :
        print ( "Bonjour le monde !" )
    elif langue == "en" :
        print ( "Hello World!" )
    else :
        print ( "Erreur : langue inconnue" )
        
        
hello_world ( "fr" )
hello_world ( "en" )
hello_world ( "de" )