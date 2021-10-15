#Funcao Factorial
def fatorial(n, show=False):
    """
    -> Call
    :param n:
    :param show:
    :return:
    """
    f = 1
    for c in range (n, 0, -1):
        if show:
            print(c, end='')
            if c>1:
                print(' x ', end='')
            else:
            #print(f'{c} X ')
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, show=True))   # 5 x 4 x 3 x 2 x 1 = 120 Show is me mostre com o calculo
#print(fatorial(5, show=False))  # 120 show mostra apenas o resultado
#print(fatorial(5))              # 120 mostra apenas o resultado
#print(fatorial(5,True))         # 5 x 4 x 3 x 2 x 1 = 120  mostra com o calculo
help(fatorial)                 # mostra o help como usar o modulo factorial