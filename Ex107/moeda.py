def aumentar(preco, taxa):
    res = preco + (preco * taxa/100) # 20% do preco
    return res

def dimimuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return res

def dobro(preco):
    res = preco * 2
    return res

def metade(preco):
    res = preco / 2
    return res
