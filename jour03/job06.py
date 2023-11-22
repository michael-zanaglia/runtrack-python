def value(nombre) :
    if nombre < 0 :
        print("Le nombre est négatif.")
    elif nombre > 0 :
        print("Le nombre est positif.")
    else :
        print("Le nombre est 0.")
       
count = 0

while count < 5 :
    count += 1
    a = int(input("Entrez un nombre : "))  
    value(a)