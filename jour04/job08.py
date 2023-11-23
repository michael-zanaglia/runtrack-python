L = [8, 24, 48, 2, 16, 9, 7, 84, 91]
l = []
count = 0
for i in L :
    if i % 2 == 0 :
        count += 1
        l.append(i)

print(l,"La somme est :", sum(l))