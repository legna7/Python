def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    #
    if idade < 16:
        return f'com {idade} anos: NAO VOLTA. '
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos:VOTO OPCIONAL. '
    else:
        return f'com {idade} anos: VOTO OBRIGATORIO.'

#principal
nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))
#mes = date.today().month