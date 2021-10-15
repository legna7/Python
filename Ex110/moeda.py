def aumentar(preco = 0, taxa = 0, format=False):
    '''

    :param preco:
    :param taxa:
    :param format:
    :return:
    '''
    res = preco + (preco * taxa/100) # 20% do preco
    return res if format is False else moeda(res)

def dimimuir(preco = 0, taxa = 0, format=False):
    res = preco - (preco * taxa/100)
    return res if format is False else moeda(res)

def dobro(preco = 0, format=False):
    res = preco * 2
    return res if format is False else moeda(res)

def metade(preco = 0, format=False):
    res = preco / 2
    return res if format is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace ('.',',')

def resumo(preco=0, taxaAumento = 10, taxaReducao = 5):
    print('-=' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-=' * 30)
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco,True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'Com {taxaAumento}% de auento: \t{aumentar(preco, taxaAumento, True)}')
    print(f'Com {taxaReducao}% de reducao: \t{aumentar(preco, taxaReducao, True)}')
    print('-=' * 30)