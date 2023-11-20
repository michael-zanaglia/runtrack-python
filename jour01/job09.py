#creation de plusieurs listes pour chaque elements
liste_name = []
liste_price = []
liste_stock = []

# Tant que je n'ai pas fini je rentre une information pour chaque element et je les tri.
while True :
    name = input("Entre le nom de votre article : ")
    liste_name.append(name.capitalize())
    price = float(input("Entrez le prix de votre article : "))
    liste_price.append(price)
    stock = float(input("Entre la quantité stocké : "))
    liste_stock.append(stock)
    leave = input("Si vous avez finis entrez 'done' : ")
    if leave == "done" :
        break
    else :
        continue
        
#Recapitulatif de mes elements popur chaque liste.
print("Mes listes .")
print(f"Mes articles: {liste_name}")
print(f"Prix Unitaires: {liste_price} euro(s)")
print(f"Stocks: {liste_stock}")

#Je retire de mon stock que je souhaite prendre et je met a jour le prix unitaire et je fais mon total.
print("")
minus = int(input("Combien souhaitez vous en prendre ? "))
stock = stock - minus
print(f"il vous reste pour l'article {name}, une quantite égale à {stock}.")
price = price + (price*10/100)
total = price * minus
print(f"Il y a eu une inflation, alors votre prix total est de {total} euro(s).")

#J'affiche mon element mis à jour.
print("")
print("Mis à jour :")
print(f"Nom de l'article: {name.capitalize()}")
print(f"Prix Unitaire apres inflation: {price} euro(s)")
print(f"Stock restant: {stock}")

