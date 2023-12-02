def calcul(a,b):
    p = 1
    for i in range(b):
        p = p*a
    print("Le resultat est -->",p)

print("------> Debut du programme <------", ('\n'))

question1 = input("Entrer un chiffre :")
question2 = input("entrer la puissance :")

try:
    question1 = int(question1)
    question2 = int(question2)

    if question1 < 0:
        print("Erreur, veuillez entrer un entier positif.")
    elif question2 < 0:
        print("Erreur, veuillez entrer un entier positif.")
    else:
        calcul(question1,question2)
except:
    print("Erreur, veuillez entrer un nombre valide.")

print(("\n"), "------> fin du programe <------")





