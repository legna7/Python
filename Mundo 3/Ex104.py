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


# programa principal
n = leiaInt("Digite um numero:  ")
print(f'Voce digitou o numero {n}.')