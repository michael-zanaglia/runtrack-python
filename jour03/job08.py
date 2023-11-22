def sais(type, saison) :
    if type == "fruits" and saison == "hiver" :
        print("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "ete" :
        print("poire, fraise, cassis")
    elif type == "legume" and saison == "ete" :
        print("cartichaut, aubergine, navet")
    elif type == "legume" and saison == "hiver" :
        print("carotte, topinambour, endive")
    else :
        print("Entrez pour type 'fruits' ou 'legume' et pour saison 'hiver ou 'ete' uniquement.")


eat = input("Entrz le mot 'fruits' ou 'legume' : ")
hiet = input("Entrz le mot 'hiver' ou 'ete' : ")
sais(eat.lower(), hiet.lower())