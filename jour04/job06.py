L = [1, 2, 3, 4, 5]
l = []
l.append(L[-1])
l.extend(L[1:4])
l.append(L[0])
print(L, l)