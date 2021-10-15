aluno = dict()
aluno ['nome'] = str(input('Nome: '))
aluno ['media'] = float(input('media: '))

if aluno['media'] >= 7:
    aluno['situation'] = "approved"
elif 5 <= aluno['media'] < 7:
    aluno['situation'] = "recuperaded"
else:
    aluno['situation'] = "reprovado"

print(aluno)
for k, v in aluno.items():
    print(f'{k} = {v}')