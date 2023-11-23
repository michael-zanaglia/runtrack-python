L = []
while True : 
    while True :
        note = float(input("Inserez une note : "))
        if note > 100 :
            print("La note ne doit pas etre superieur a 100.")
        else :
            L.append(note)
            break
    
    yn = input("Voulez vous stopper ? (y/n) ")
    if yn.lower() == "y" :
        break
    elif yn.lower() == "n" :
        continue
    else :
        print("Inserez un choix valide.")
    
    
for x in L :
    if (x+2) % 5 == 0 :
        ind = L.index(x)
        L[ind] = x+2
    elif (x+1) % 5 == 0 :
        ind = L.index(x)
        L[ind] = x+1
    
        
tot = sum(L)
moy = tot / len(L)

if moy < 40 :
    print(f"RECALER, votre moyenne est de {moy}. Vos notes apres analyse sont les suivantes : {L}")
else :
    print(f"REUSSI, votre moyenne est de {moy}. Vos notes apres analyse sont les suivantes : {L}")