import string

def code() :
    lm = []
    la = []
    final = ""
    message = input("Ecrivez votre message secret ! -: ") 
    alpha = string.ascii_lowercase
    lm = message.lower().split(" ")
    for letters in alpha :
        la.append(letters)
    for words in lm :
        for letter in words :
            if letter in la :
                ind = (la.index(letter) + 3) % 26
                final += la[ind] 
            else :
                final += letter
        final += " "  
    return final
    
secret = code()
print(secret.capitalize())