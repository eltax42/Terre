while True:

    question = input("Ecrivez un lettre de l'alphabet :")

    if len(question) == 1 and'a' <= question <= 'z':

        for i in range(ord(question), ord('z') + 1):
            print(chr(i), end='')
        break

    else:
         print("Veuillez saisir UNE minuscule (a->z)")

print('\n')