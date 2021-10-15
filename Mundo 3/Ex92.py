from datetime import datetime
dados = dict()
dados['nome'] = str(input('nome: '))
nasc = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS']: int(input('Carteira de trabalho (0 nao possui carteira): '))
if ['CTPS'] != 0:
    dados['contratacao'] = int(input('ano da contratacao: '))
    dados['salario'] = float(input('salario: '))
    dados['aposentadoria'] = dados ['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f'{k} = {v}')




