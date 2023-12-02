def calcul():
    b = 2
    
    if a%b == 0:
        print("Votre chiffre est Pair .")   
    else:
        print("Votre chiffre est Impair .")    
    
print("------> Debut du programme <------", ('\n'))
a = input("Ecrivez un nombre entier : ")

try:
    a = int(a)
    calcul()
except:
    print("Erreur ! Entrez un nombre entier !")

print(("\n"), "------> fin du programe <------")

