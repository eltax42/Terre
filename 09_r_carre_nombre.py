def r_carre(a):
    return a ** 0.5

print("------> Debut du programme <------", ('\n'))

try:
    Question = int(input("Ecrire un chiffre entier -->"))
    if Question == 0:
        print("Le Fameux zero")
    else:
        Resultat = r_carre(Question)
        Resultat_f = "{:.3f}".format(Resultat)
        print(f"La racine carre de {Question} est {Resultat_f}")
except ValueError:
    print("Erreur, ce n'est pas un nombre entier.")

print(("\n"), "------> Fin du programe <------")
