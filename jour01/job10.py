amount = float(input("Montant :"))
rate = 2
total = amount + (amount*(2/100))

print(total)


while True :
    yes = input("Souhaitez vous retirer 10% de votre capitale ?(y/n) ")
    if yes.lower() == "y" :
        amount = amount - (amount*10/100)
        rate = 1
        tot = amount + (amount*(1/100))
        print(f"Le montant annuel pour un rendement de {rate} est : {tot}")
        break
    elif yes.lower() == "n" : 
        break
    else :
        print("Error : Veuillez entrez uniquement 'y' ou 'n'.")
        continue
    