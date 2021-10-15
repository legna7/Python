# desapacotamento de paramentros em funcoes
from time import sleep

def maior(* num):
# receber varios paramentos para desempacotar
    cont = maior = 0
    print('-='*30)
    print('\nAnalisando os valores passados... ')
    for valor in num: # mostrar os numeros
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor # maior receber o valor
        else:
            if valor > maior:
                maior = valor
        cont += 1 # tem mais um numero
    print(f'Foram invormados {cont} valores ao todo ')
    print(f'O maior valor informatio foi {maior}.')



#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()