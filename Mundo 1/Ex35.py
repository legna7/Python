import math
while True:
    r1 = float(input('Tamanho da reta(em cm): '))
    r2 = float(input('Tamanho da reta(em cm): '))
    r3 = float(input('Tamanho da reta(em cm): '))
    if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r2 + r1):
        print('Medidas satisfatorias para o triangulo!')
        break
    else:
        print('Medidas nao satisfatorias para o triangulo. ')
        print('Tente novamente')
        print('')