def calcul(a):
    c=0
    for i in range(1,a+1):
        if a%i == 0:
            c = c + 1
    if c == 2:
        print(f"{a} est un nombre premier")
    else:
        print(f"{a} n'est pas un nombre premier, divisable ({c})fois")

print("------> Debut du programme <------", ('\n'))

try:
    Question_user = int(input("Ecrivez un nombre entier :"))
    if Question_user <= 1:
        print("Erreur, pas en dessous de 2 les nombres premiers !")
    else:
        calcul(Question_user)
except ValueError:
    print("Erreur, ce n'est pas un nombre entier")

print(("\n"), "------> Fin du programe <------")
