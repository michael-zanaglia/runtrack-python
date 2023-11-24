l = [90, 22, 12, 34, 64, 11, 25]

def my_sort(L):
    # Je mets en place mon compteur 
    count = 0
    # Tant que L est different du resultat de sorted(L) :
    while L != sorted(L):
        # J'incremente de 1 pour chaque boucle
        count += 1
        # Pour j dans ma range (ici 0, 6-1)
        for j in range(0, len(L)-1) :
            # Si mon index est superieur au suivant alors je les intervertis. Le -1 dans le for 
            # est important sinon j'aurais une value error index out of range.
            if L[j] > L[j+1] :
                L[j], L[j+1] = L[j+1], L[j]
    print("Nombre total de coup nécéssaire pour trier la liste :", count)
    print("Liste triée :", L)
        
    

my_sort(l)