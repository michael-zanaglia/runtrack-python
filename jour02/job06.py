for i in range (1, 1001):
    # les nombre premier sont uniquement divisible par 1 ou eux meme.
    # 1 n'est pas un nombre premier donc on passe a la suite.
    if i > 1 :
    # pour chaque nombre dans la range donnee, si un nombre ou chiffre dans
    #la range donne un reste de 0 alors il n'est pas premier et on passe a la suite.
        for x in range (2, i):
            if (i % x) == 0 :
                break
        else :
            print(i)