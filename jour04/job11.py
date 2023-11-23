L = [7, 11, 42, 39, 2]
lenght = len(L)
print("Liste de départ :", L)
while True :
    yn = input("Souhaitez vous incrementer de 1 chaque valeur de votre liste ? (y/n) ")
    if yn.lower() == "y" :
        for i in range(lenght) :
            L[i] = L[i] + 1
        print(L)
    elif yn == "n" :
        break
    else : 
        print("Entrez une réponse valide.")