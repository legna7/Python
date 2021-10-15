#from ex109 import moeda
import moeda

p = float(input('Digite o preco: R$ '))
print(f'A metade de R${moeda.moeda(p)} eh {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} eh {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10, True)}')
print(f'Reduzingo 13%, temos R${moeda.dimimuir(p,13,True)})')