def add(x,z) :
    print(f"{x} + {z} = {x + z}")
       
count = 0

while count < 5 :
    count += 1
    a = int(input("Entrez un nombre : "))  
    b = int(input("Entrez un deuxieme nombre : "))  
    add(a,b)