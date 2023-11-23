def my_long_word():
    while True :
        try :
            x = int(input("Definissez un nombre : "))
            break
        except ValueError :
            print("Entrez un nombre entier valide:")
            continue
    c = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
    c = c.replace(",", " ")
    c = c.split()
    chaine = []
    count = 0
    for word in c :
        if len(word) > x :
             chaine.append(word)
             count += 1
    
    return x, chaine, count



nbre, stings, count = my_long_word()
if count == 0 :
    print(f"Aucun mot n'est plus long que {nbre}.")
else :
    print(nbre, " ".join(stings))