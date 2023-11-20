string = input("Entrez un mot: ")
nbr_e = 0

for i in string :
    if i == "e" :
        nbr_e += 1

if nbr_e > 0 :
    print("Vous avez au moins un 'e' dans votre mot.")
    print(f"Dans votre mot {string} vous avez {nbr_e} 'e'.") 
else :
    print(f"Vous n'avez pas de 'e' dans votre mot {string}")

        