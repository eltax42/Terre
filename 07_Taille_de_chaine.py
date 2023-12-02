def t_chaine(a):
    n_lettres = 0
    for lettre in a:   
        n_lettres += 1
    print("La taille de la chaine est --> ",n_lettres)

print("------> Debut du programme <------", ('\n'))

Message = input("Ecrivez un message --> ")
t_chaine(Message)

print(("\n"), "------> fin du programe <------")