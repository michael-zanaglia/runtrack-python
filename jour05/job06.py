stairs = int(input("Combien de marche ? "))
h = float(input("Combien de cm par marche ? "))

def hauteur(x, y) :
    ym = y / 100
    xy = (x * ym) * 2
    jour = xy * 5
    total = jour * 7
    print (f"Pour {x} marches de {y}cm, le gardien parcourt {total:.2f}m par semaine.")


hauteur(stairs, h)