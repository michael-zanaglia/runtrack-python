L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
l = []
mult = 1
for i in L :
    if i >= 25 and i <= 90 :
        l.append(i) 
for x in l :
    mult *= x
print(f"Dans ma plage [25,90] j'obtiens cette liste-ci : {l}. En les multipliant, j'obtiens :", mult)