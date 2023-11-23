#1.0

phrase = input("Ecrivez un message --> ")

for i in range(len(phrase)-1,-1,-1):
    print(phrase[i], end='')
print('\n')