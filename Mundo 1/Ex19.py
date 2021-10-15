from random import choice
a1 = str(input('digite nome do aluno1: '))
a2 = str(input('digite nome do aluno2: '))
a3 = str(input('digite nome do aluno3: '))
a4 = str(input('digite nome do aluno4: '))
a5 = str(input('digite nome do aluno5: '))
lista = [a1,a2,a3,a4,a5]
escolhido = choice(lista)
print(' o aluno escolhido {}.'.format(escolhido))