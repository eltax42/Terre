def r_ligne(a):
    for each_w in a:
        print(each_w)

print("------> Debut du programme <------", ('\n'))

Question = input("Ecris ce que tu veux : ")
Question = Question.split()

r_ligne(Question)

print(('\n'),"------> fin du programe <------")