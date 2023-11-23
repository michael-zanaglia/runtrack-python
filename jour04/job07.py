L = [8, 24, 48, 2, 16]
l = []
count = 0
for i in L :
    if i % 3 == 0 :
        count += 1
        l.append(str(i)) #je ne peux join uniquement des strings.
print(f"Dans cette liste il y a {count} multiple(s) de trois. Voila ce(s) dernier(s) :", ", ".join(l))