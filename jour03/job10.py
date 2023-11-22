def value(nombre) :
    if (nombre % 2) == 0 :
        print("Le nombre est paire.")
    else :
        print("Le nombre est impaire.")
       
count = 0

while count < 5 :
    a = input("Entrez un nombre : ")  
    try :
        a = int(a)
        value(a)
        count += 1
    except ValueError :
        print("Entrz un nombre entier et positif.")