#1.0

while True:
    try:
        Nombre1 = int(input("Entrez un nombre: "))
        break
    except:
        print("Veuillez entrer un nombre !")

while True:
    try:
        Nombre2 = int(input("Entrez un deuxieme nombre: "))
        break
    except:
        print("Veuillez entrer un nombre !")

        
if Nombre2 > Nombre1:
            print("Le premier Nombre doit etre superieur !")
else:
    calcul = Nombre1 / Nombre2
    calcul = int(calcul)
    Reste = Nombre1 % Nombre2
    print("Le resultat est",calcul ,"et il reste ",Reste,".")