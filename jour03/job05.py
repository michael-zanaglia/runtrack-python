def calcule(num1, operator, num2) :
    if operator == "+" :
        print(f"Trouvez le resultat de l'addition : {num1} {operator} {num2} = {num1 + num2}")
    elif operator == "-" :
        print(f"Trouvez le resultat de la soustraction : {num1} {operator} {num2} = {num1 - num2}")
    elif operator == "x" or operator == "*" :
        print(f"Trouvez le resultat de la multiplication : {num1} {operator} {num2} = {num1 * num2}")
    elif operator == "/" :
        print(f"Trouvez le resultat de la division : {num1} {operator} {num2} = {num1 / num2}")
    elif operator == "%" :
        print(f"Trouvez le reste : {num1} {operator} {num2} = {num1 % num2}")
    else :
        print("Erreur, veuillez indiquer un caractere pour realiser une opération:")
        
a = float(input("Entrez un nombre : "))  
b = input("Entrez votre caractere pour l'opération : ")  
c = float(input("Entrez un nombre : "))         

calcule(a,b,c)