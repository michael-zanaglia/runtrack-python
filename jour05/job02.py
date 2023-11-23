def my_rectangle(x, y) :      
    coordonate = (x, y)
    print(coordonate)
    z = y -1
    for i in range(y) :
        if i == 0 or i == z :
            print("|"+("-"*x)+"|")
        else :
            print("|"+" "*x+"|")
            
my_rectangle(10,3)