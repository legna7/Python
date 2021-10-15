def leiaInt(msg):
    #ok = False
    #valor = 0
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um numero real valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um numero real valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n

# programa principal
n1 = leiaInt("Digite um numero:  ")
n2 = leiaFloat('Digite um Real: ')
print(f'Voce digitou o valor inteiro {n1} e o real foi {n2}')

