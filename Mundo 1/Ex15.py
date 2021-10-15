km=float(input('Quantos km percorridos: '))
d = float(input('Quantos dias alugado: '))

pago = (d * 60) + (km * 0.15)
print('o total a pagar: r$ {} '.format(pago))
