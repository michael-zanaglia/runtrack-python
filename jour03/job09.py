def moyenne(x, y, z):
    average = (x+y+z)/3
    return average

note1 = float(input("Entrez une première note : "))
note2 = float(input("Entrez une seconde note : "))
note3 = float(input("Entrez une troisième note : "))
average = moyenne(note1, note2, note3)


if average >= 15 :
    print(f"Très bon éleve : {average} de moyenne.")
elif average >= 11 and average < 15 :
    print(f"Bon éleve : {average} de moyenne.")
elif average >= 7 and average < 11 :
    print(f"Eleve moyen : {average} de moyenne.")
elif average < 8 :
    print(f"Eleve devant faire des efforts : {average} de moyenne.")
