L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
lenght = len(L)
l = []
print(L)
for x in L :
    #si x qui a une valeur ici n'est pas deja dans l alors ajoute le.
    if x not in l :
        l.append(x)
print(l)