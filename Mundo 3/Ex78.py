listanum = []
maior = menor = 0
for c in range (0,5): #cria 5 valores
    listanum.append(int(input(f'Digite um valor para a posicao {c}: '))) #
    if c==0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(' = ' *30)
print(f'Voce digitou os valores {listanum} ')
print(f'O valor maior digitado {maior} na posicao ', end = '')
for i, v in enumerate(listanum): # print out the index posicao
    if v == maior:
        print (f'{i}...', end = '')
print(f'O valor menor digita {menor} na posicao ', end = '')
for i, v in enumerate(listanum): # print out the index posicao
    if v == menor:
        print (f'{i}...', end = '')
print()
