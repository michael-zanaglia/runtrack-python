def listes(l):
    print(l)
    r = len(l)
    for i in range(r) :
        #le -i-1 permet de faire le +1 
        for j in range(0, r-i-1):
            if l[j] > l[j+1] :
                l[j], l[j+1] = l[j+1], l[j]
    return l
        
    
L = []    
while True :
    try :
     a = int(input("Entrez une valeur : "))
    except ValueError :
         print("Entrez un nombre entier")
         continue
    L.append(a)
    yn = input("Voulez vous continuer ?(y/n) ")
    if yn.lower() == "n" :
        break
    elif yn.lower() == "y" :
        continue
listes(L)

print(L)       
        
#Je dois comparer mes indexes pour echanger les nombres si l'un est plus grand que l'autre.
#Pour ce faire je dois avoir une variable i pour modifier ma range a chaque iterations.
#le -1 me permet des le debut d'eviter l'erreur out of range lors de mes comparaisons.
#En prenant en compte tout ca le j+1 de depassera pas de ma range et je pourrais comparer mes elements.
    