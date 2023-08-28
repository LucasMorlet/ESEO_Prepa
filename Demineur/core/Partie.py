from Grille import *
from Input import *

class Partie :
    
    def __init__ ( self, w, h, n ) :
        self.grille = Grille ( 5, 5, 5 )
        self.nbCasesAReveler = w*h-n
        self.etat = 'e' # e : en cours, g : gagne, p : perdu
        self.interaction = Input()
        
    def afficheGrille ( self ) :
        print()
        self.grille.afficheConsole()
        print()
        
    def testVictoire ( self ) :
        if ( self.grille.getNbCasesVisible() >= self.nbCasesAReveler ) :
            self.etat = 'g'
          
    def joue ( self ) :
    
        # Boucle principale
        while ( self.etat == 'e' ) :
            self.afficheGrille()
            print ( 'Quelle action voulez-vous effectuer ?', end = ' ' )
            string = input()
            self.interaction.traiteString ( string )
                      
            if ( not self.interaction.isErreur() ) :
                i = self.interaction.getCaseI()
                j = self.interaction.getCaseJ()
                action = self.interaction.getAction()
                if ( not self.grille.estUneCaseValide ( i, j ) ) :
                    print ( "En dehors de la grille !" )
                elif ( action == 'r' ) :
                    self.grille.reveleCase ( i, j )  
                    if self.grille.isBombe ( i, j ) :
                        self.etat = 'p'
                    else :
                        self.testVictoire()   
                elif ( action == 'd' ) :
                    self.grille.switchDrapeau ( i, j )
                    
        # Conclusion
        if ( self.etat == 'g' ) :
            print ( "Victoire !" )
        else :
            print ( "Perdu !" )
            
        self.grille.reveleTotalite()
        self.afficheGrille()
                                  
    