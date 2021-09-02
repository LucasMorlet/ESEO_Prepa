# Extrait le chiffre en position <puiss> en démarrant de la droite (0 -> unité)
def extraire_chiffre ( n, puiss ) :
    return int ( n / 10**puiss ) % 10

class Boulier :

    def __init__ ( self ) :
        self.millier  = 0
        self.centaine = 0
        self.dizaine  = 0
        self.unite    = 0

    def afficher_valeur ( self ) :
        print ( " ", self.millier, self.centaine, self.dizaine, self.unite )

    def set_valeur ( self, n ) :
        self.unite    = extraire_chiffre ( n, 0 )
        self.dizaine  = extraire_chiffre ( n, 1 )
        self.centaine = extraire_chiffre ( n, 2 )
        self.millier  = extraire_chiffre ( n, 3 )
        
    def get_valeur ( self ) :
        return self.millier * 1000 + self.centaine * 100 + self.dizaine * 10 + self.unite
        
    def ajouter_unite ( self, u ) :
        res = u + self.unite
        if ( res < 10 ) :
            self.unite = res
        else :
            self.unite = res % 10
            self.ajouter_dizaine ( 1 )
            
    def ajouter_dizaine ( self, d ) :
        res = d + self.dizaine
        if ( res < 10 ) :
            self.dizaine = res
        else :
            self.dizaine = res % 10
            self.ajouter_centaine ( 1 )
            
    def ajouter_centaine ( self, c ) :
        res = c + self.centaine
        if ( res < 10 ) :
            self.centaine = res
        else :
            self.centaine = res % 10
            self.ajouter_millier ( 1 )
            
    def ajouter_millier ( self, m ) :
        res = m + self.millier
        if ( res < 10 ) :
            self.millier = res
        else :
            print ( "Depassement de mémoire !" )
            self.set_valeur ( 0 )
     
    def retirer_unite ( self, u ) :
        if ( self.unite >= u ) :
            self.unite -= u 
        else :
            self.unite += 10 - u
            self.retirer_dizaine ( 1 )
            
    def retirer_dizaine ( self, d ) :
        if ( self.dizaine >= d ) :
            self.dizaine -= d 
        else :
            self.dizaine += 10 - d
            self.retirer_centaine ( 1 )
            
    def retirer_centaine ( self, c ) :
        if ( self.centaine >= c ) :
            self.centaine -= c 
        else :
            self.centaine += 10 - c
            self.retirer_millier ( 1 )
            
    def retirer_millier ( self, m ) :
        if ( self.millier >= m ) :
            self.millier -= m
        else :
            self.set_valeur ( 0 )
            print ( "Depassement de mémoire !" )
            
        
    def ajouter_valeur ( self, n ) :
        self.ajouter_unite    ( extraire_chiffre ( n, 0 ) )
        self.ajouter_dizaine  ( extraire_chiffre ( n, 1 ) )
        self.ajouter_centaine ( extraire_chiffre ( n, 2 ) )
        self.ajouter_millier  ( extraire_chiffre ( n, 3 ) )
        
    def retirer_valeur ( self, n ) :
        self.retirer_unite    ( extraire_chiffre ( n, 0 ) )
        self.retirer_dizaine  ( extraire_chiffre ( n, 1 ) )
        self.retirer_centaine ( extraire_chiffre ( n, 2 ) )
        self.retirer_millier  ( extraire_chiffre ( n, 3 ) )
        
    def multiplier_par_valeur ( self, n ) :
        if ( n == 0 ) :
            self.set_valeur ( 0 )
        else :
            val = self.get_valeur()
            for i in range ( n-1 ) :
                self.ajouter_valeur ( val )
                
    def diviser_par_valeur ( self, n ) :
        i = 0
        while ( self.get_valeur() > n ) :
            i += 1 
            self.retirer_valeur ( n )
        return i
    
def main ( ) :
    boul = Boulier()
    choix = ''
    while ( choix != '0' ) :
        print ()
        boul.afficher_valeur()
        print ()
        print ( "1 - Définir la valeur" )
        print ( "2 - Ajouter une valeur" )
        print ( "3 - Soustraire une valeur" )
        print ( "4 - Multiplier par une valeur" )
        print ( "5 - Diviser par une valeur" )
        print ( "0 - Quitter" )
        print ()
        choix = input ( "Votre choix ? " )
        print()
        
        if ( choix == '1' ) :
            n = int ( input ( "Nombre à définir ? " ) )
            boul.set_valeur ( n )
            
        elif ( choix == '2' ) :
            n = int ( input ( "Nombre à ajouter ? " ) )
            boul.ajouter_valeur ( n )
            
        elif ( choix == '3' ) :
            n = int ( input ( "Nombre à soustraire ? " ) )
            boul.retirer_valeur ( n )
            
        elif ( choix == '4' ) :
            n = int ( input ( "Nombre à multiplier ? " ) )
            boul.multiplier_par_valeur ( n )
            
        elif ( choix == '5' ) :
            n = int ( input ( "Nombre par lequel diviser ? " ) )
            q = boul.diviser_par_valeur ( n )
            print ( "Resultat : q =", q, "r =", boul.get_valeur() )
            
        else :
            print ( "Choix non-défini" )

main()

# Amélioration possible, remplacer les attributs par un tableau unique
# => on peut fusionner les fonctions redondantes