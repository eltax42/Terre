def mots(a):
    for lettre in range(len(a)-1,-1,-1):
        print(a[lettre],end='')

print("------> Debut du programme <------", ('\n'))

question = input("Ecrivez ici --> ")

if len(question) == 0:
    print('Erreur')
    print('\n')
else:
    mots(question)
    print('\n')

print("------> Fin du programe <------")