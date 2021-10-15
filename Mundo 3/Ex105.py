def notas(*n, sit=False):
    """
    --> Funcao para analisar notas, e situacoes de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adcionar a situacao
    :return: dicionario com varias informacoes sobre a situacao da turma.
    """
    r = dict() #dicionario
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['media'] = 'BOA'
        elif r['media'] >= 5:
            r['situation'] = 'RAZOAVEL'
        else:
            r['situation'] = 'RUIM'
    return r

# program principal
resp = notas(5.5,2.5,9,8.5, sit=True)
print(resp)
help(notas)