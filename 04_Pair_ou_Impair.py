#1.1

a = input("Ecrivez un nombre: ")
b = 2
try:
    a = int(a)
    if a%b == 0:
        print("Votre chiffre est Pair")
    else:
        print("Votre chiffre est Impair")
except:
    print("Vous devez entrer un Nombre !")



