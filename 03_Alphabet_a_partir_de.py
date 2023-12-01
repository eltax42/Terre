def alph_a_partir_de(a):

    if len(a) == 1 and 'a' <= a <= 'z':
        for lettre in range(ord(a) , ord("z") +1):
            print(chr(lettre) , end='')
        print('\n')
    else:
        print("Erreur")
        print('\n')

print("------> Debut du programme <------", ('\n'))
            
question = input("Ecrivez un lettre de l'alphabet en minuscule :")

alph_a_partir_de(question)

print("------> fin du programe <------")