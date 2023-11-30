def calcul(a,b):
    
    if a == 0 or b == 0:
        print("Une division de 0 est impossible")
    else:
        c = 0
        while a >= b:
            a -= b
            c += 1
        print(f"Le resultat est : {c} ,reste {a}.")



print("------> Debut du programme <------", ('\n'))

dividende = input("Ecrivez le dividende :")
diviseur = input("Ecrivez le diviseur :")       


try:
    dividende = int(dividende)
    diviseur = int(diviseur)
    calcul(dividende,diviseur)
except:
    print("Erreur,Veuillez entrer des nombres(entiers)")

print(("\n"), "------> fin du programe <------")


  



