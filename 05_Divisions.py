def calcul(a,b):
    c = 0
    if a or b == 0:
        print("erreur")
    else:
        while a >= b:
            a -= b
            c += 1
        print(c,a)

dividende = input("Ecrivez le dividende :")
diviseur = input("Ecrivez le diviseur :")       

try:
    dividende = int(dividende)
    diviseur = int(diviseur)
except:
    print("erreur")

calcul(dividende,diviseur)









