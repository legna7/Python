from Ex115.lib.interface import *
from Ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    #print('Arquivo encontradon com sucesso!')
#else:
    #print('Arquivo nao encontrado')

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar novas pessoas', 'Sair do sistema'])
    if resposta == 1:
        # opcao de listar o conteudo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho ('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema...Ate logo!')
        break
    else:
        print('\033[mERRO! Digite uma opcao valida!\033[m')
        sleep(2)

