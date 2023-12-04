def convertisseur(a):
    try:
        b,c = map(int,a.split(':'))
        if b >= 24:
            print("Erreur, il n'y a que 24h dans une journée !")
        elif b > 12:
            b = b -12
            heure_12 = "{:02d}:{:02d}".format(b,c)
            print(heure_12,"PM")
        elif b < 0:
            print("Erreur, voici un exemple (17:42)")
        else:
            print(a,"AM")
    except ValueError:
        print("Erreur, voici un exemple (16:28)")

print("------> Debut du programme <------", ('\n'))

Question_user = input("Ecrivez une heure sous le format 24h (HH:MM) : ")
convertisseur(Question_user)

print(("\n"), "------> Fin du programe <------")