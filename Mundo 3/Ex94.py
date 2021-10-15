
galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa ['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo']=str(input('Sexo: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')

    while True:
        try:
            pessoa['idade']=int(input('idade: '))
        except ValueError:
            print('Digite um valor numerico.')
        else:
            break
    soma += pessoa['idade']

    galera.append(pessoa.copy())
    while True:
        resp=str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N. ')
    if resp == 'N':
        break

print(galera)

print('-='*30)
print(f'a) Ao todo temos {len(galera)} pessoa cadastradas.')

media = soma / len(galera)
print(f'b) A media de idade eh de {media:5.2f} anos.')
print(f'c) As mulhere cadastradas foram ', end='')
for individuo in galera:
    if individuo['sexo'] in 'Ff':
        print(f'{individuo["nome"]} ', end='')
print()

print(f'd) Lista das pessoas que estao acima da media: ')
for individuo in galera:
    if individuo['idade'] >= media:
        print('  ')
        for k,v in individuo.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO>>')



