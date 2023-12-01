import os

def nom_du_fichier():
    fichier = os.path.basename(__file__)
    print("Nom du fichier --> ", fichier)

print("------> Debut du programme <------", ('\n'))

nom_du_fichier()

print(('\n'),"------> fin du programe <------")

