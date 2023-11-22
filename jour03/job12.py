def reverse(string) :
    liste = []
    for x in reversed(string) :
        liste.append(x)
    print("Ton mot à l'envers :", "".join(liste))
        
try :            
    strings = str(input("Entrez un mot : "))
    reverse(strings)
except ValueError :
    print("Entrez un mot et non un nombre.")