nome = str(input('Qual o seu nome completo: ')).strip().lower()
print(nome)
#print('seu nome tem Silva? {}.'.format(nome[:4]=='silva'))
print('seu nome tem Silva? {}.'.format('silva'in nome.lower()))