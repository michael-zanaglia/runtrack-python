a = int(input("Entrez la longueur de a : ")) 
b = int(input("Entrez la longueur de b : "))
c = int(input("Entrez la longueur de c : "))

def rect(x,y,z) :
    if x^2 == y^2 + z^2 :
        print("C'est un trinangle rectangle")
    else :
        print("C'est un triangle quelconque.") 


if a <= b + c and b <= a + c and c <= a + b :
    print("Le triangle est constructible.")
    if a == b or a == c or b == c :
            if a == b and b == c :
                print("Le triangle est équilatéral.")
            else :
                print("C'est un triangle isoscele.")
            if a^2 == b^2 + c^2 or b^2 == a^2 + c^2 or c^2 == a^2 + b^2 :
                print("Le triangle est isocele rectangle.")   
    elif a > b and a > c  :
        print("a est la plus grande valeur.")
        rect(a,b,c)
    elif b > a and b > c :
        print("b est la plus grande valeur.")
        rect(b,a,c)    
    elif c > a and c > b :
        print("c est la plus grande valeur.")
        rect(c,a,b)
else :
    print("Le triangle n'est pas constructible.")

