def tapis(x) :
    for i in range(x) :
        if i == 0 :
            print("|"+("#"*x)+(" "*1)+"|")
        else :
            print("|"+("#"*(x-i))+(" "*1)+("#"*i)+"|")
    print("|"+(" "*1)+("#"*x)+"|")
            
    



n = int(input("Entrez une valeur : "))

print("+"+("-"*(n+1))+"+")
tapis(n)
print("+"+("-"*(n+1))+"+")