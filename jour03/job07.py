def name(langage) :
    if langage == "Javascript" :
        print("Tu es un développeur web.")
    elif langage == "Python" :
        print("Tu es un développeur IA.")
    elif langage == "Java" :
        print("Tu es un développeur logiciel.")
    elif langage == "Reactjs" :
        print("Tu es un développeur mobile.")
    else :
        print("Un jour je serais le meilleur développeur...")
        


count = 0

while count < 5 :
    count += 1
    code = input("Entrez un langage : ")
    name(code.capitalize())