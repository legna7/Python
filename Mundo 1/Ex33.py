salario = float(input('digite o seu salario: '))
aumento = (salario + (salario * 15)/100 if salario <= 1250 else salario + (salario * 10)/100)
print(aumento)