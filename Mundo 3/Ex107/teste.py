import moeda
#import ex107.moeda

p = float(input('Digite o preco: R$ '))
print(f'A metade de R${p} eh {moeda.metade(p)}')
print(f'O dobro de {p} eh {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')