def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg} x {comp} eh de {a} m2.')

print('Controle de Terrenos')
print('-='*20)
l = float(input('Largura (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)
