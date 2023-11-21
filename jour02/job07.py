import string

string = string.ascii_lowercase
lea=len(string)

#pour chaque i associe a un chiffre, il afichera l'index de 0 à i ce qui fera une suite pyramidale
for i in range (lea+1) :
        print(string[:i])



#pour faire une vrai pyramide :
# print(" "*(lea - i) + string[:i]  +  string[-i:])