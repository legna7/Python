time = list()
jogador = dict() # dicionario criado
partidas = list() # lista criada para guarda os gols

while True:
    jogador.clear()
    jogador['nome'] = str(input('nome: ')) # ler o nome do jogador
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou: ')) # criou variavel
    partidas.clear()
    for c in range(0,total):
        partidas.append(int(input(f'    Quantos goals na partida {c+1}? ')))
    jogador['gols'] = partidas[:] # [:] copiou o que tem em partidas
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Responda apenas S or N.')
    if resp == 'N':
        break
print('-='*30)
#cabecalho
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
#final do cabecalho

print('-='*40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)

# qual jogador vc quer ver os resultados(busca)
while True:
    busca = int(input('Mostra dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time): # nao pode procurar jogador que nao existe
        print(f'ERRO! Nao existe jogador com codigo {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols')
print()
print('<<< VOLTE SEMPRE >>>')