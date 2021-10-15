jogador = dict() # dicionario criado

partidas = list() # lista criada para guarda os gols

jogador['nome'] = str(input('nome: ')) # ler o nome do jogador

total = int(input(f'Quantas partidas {jogador["nome"]} jogou: ')) # criou variavel
for c in range(0,total):
    partidas.append(int(input(f'    Quantos goals na partida {c}? ')))

jogador['gols'] = partidas[:] # [:] copiou o que tem em partidas
jogador['total'] = sum(partidas)
print(jogador)
#print(partidas)
print("")
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print("")
print('-='*30)
print(f'o jogador {jogador ["nome"]} jogou {len(jogador["gols"])} partidas.')
for i,v in enumerate (jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f' Foi um total de { jogador["total"]} gols.')


