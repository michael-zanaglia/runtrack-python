x = int(input("Donnez un nombre : "))
space = " " * x


# Pour i dans une range de 0 a x-1 :
for i in range(x) :
    # Si i = 0 :
    if i == 0 :
        # J'affiche le début du triangle
        print(space+"/"+ "\\")
    # Sinon si i = la fin de ma range :
    elif i == x-1 :
        # J'affiche mon pattern
        # 1 espace + / + _ * (i*2) + \
        print((" "*(x-i))+"/"+"_"*(x+i-1)+"\\")
    # Sinon :
    else :
        # J'affiche l'espace que je reduis à chaque iteration
        # ainsi que ma longueur 
        # plus l'espace interne du triangle qui fait +2 a chaque iteration
        print((" "*(x-i))+"/"+" "*(i*2)+"\\")