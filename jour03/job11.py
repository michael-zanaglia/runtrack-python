def time_to_text(x, y) :
    print(f"{x} heure(s) et {y} minute(s)")
    
while True :   
    try :
        hour = int(input("Entrez une heure : "))
        break
    except ValueError :
        print("Entrz un nombre entier et positif.")
        continue
while True :    
    try :    
        min = int(input("Entrez des minutes : "))
        break
    except ValueError :
        print("Entrz un nombre entier et positif.")   
        continue    
        
time_to_text(hour, min)
    
