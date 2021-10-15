temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()
    #resp = str(input('Quer continuar [s/n]? '))
    #if resp in 'Nn':
        #break

    while True:
        resp = str(input('Quer continuar [s/n]? ').upper().strip()[0])
        if resp in 'SN':
            break
        else:
            print('Error! Digite S or N apenas.')
    if resp == 'N':
        break

print('-=' * 30)
#print(f'Os dados digitados foram {princ}.')
print(f'Ao todo, voce digitou {len(princ)} pessoas.')

print(f'O maior peso foi {mai}kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {men}kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()