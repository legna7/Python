#from ex108 import moeda
import moeda

p = float(input('Digite o preco: R$ '))
print(f'A metade de R${moeda.moeda(p)} eh {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} eh {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(p, 10))}')