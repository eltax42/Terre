while True:

    question = input("Ecrivez un lettre de l'alphabet :")
    reponse = question

    if 'a' <= reponse <= 'z':

        for i in range(ord(reponse), ord('z') + 1):
            print(chr(i), end='')
        break

    else:
         print("Veuillez saisir une minuscule (a->z)")

print('\n')