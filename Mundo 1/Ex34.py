salary = float(input('Salario: '))
if salary > 1250.0:
    print('Seu aumento sera de R${:.2f}.'.format((salary * 1.1) - salary)) #Salario > R$1.250,00, aumente 10%
else:
    print('Seu aumento sera de R${:.2f}.'.format((salary * 1.15) - salary)) #Salario < R$1.250,00, aumente 15%
print('-=' * 30)
s = float(input('Qual o sálario do funcionário? R$'))
desc = (s * 10) / 100 if s > 1250 else (s * 15) / 100
print('O salário será {} Reais'.format(desc + s))

salary = float(input('qual eh o seu salario? '))
aumento = (salary * 10)/100 if salary > 1250 else (salary * 15)/100
print('O salario sera {:.2f}'.format(aumento + salary))
