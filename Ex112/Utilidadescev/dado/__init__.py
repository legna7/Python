def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" eh um preco invalido!\033[m')
        else:
            valido = True
            return float(entrada)



# from Ex104
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[0;33mERRO! Digite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor