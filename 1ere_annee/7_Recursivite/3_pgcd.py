def recPGCD ( a, b ) :
    if a == b : return a
    if b == 0 : return a
    return recPGCD( b, a%b )
      
a = int(input("a : "))
b = int(input("b : "))
print ( "PGCD (", a, ";", b, ") =", recPGCD ( a, b ) )