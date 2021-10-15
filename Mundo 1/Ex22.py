n = str(input('Digite um nome: ').strip()) # no espacos
print('o nome em maiusculo: {}.'.format(n.upper()))
print('o nome em minuscula: {}.'.format(n.lower()))
print("o nome tem ao tod {} letras.".format(len(n) - n.count(' ')))
n.find(' ')
print(n)
print("seu primeiro nome tem {} letras.".format(n.find(' ')))
