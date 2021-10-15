from Ex112.Utilidadescev import moeda
from Ex112.Utilidadescev import dado


#p = float(input('Digite o preco: R$ '))
p = dado.leiaDinheiro('Digite o preco: R$ ')
moeda.resumo(p, 35, 22)