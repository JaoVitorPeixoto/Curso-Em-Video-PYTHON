from DESAFIO115.bib import interface, arquivo, dado
from time import sleep

print('======== DESAFIO 115 ========')
print('')

arq = 'Lista_EX_115.txt'

if not arquivo.arquivoExiste(arq):
    print('\033[31mArquivo não encontrado!!\033[m')
    resp = str(input('\033[33mDeseja criar um novo? [S/N]\033[m')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('\033[33mInforme corretamente, deseja criar um novo? [S/N]\033[m')).strip().upper()[0]

    if resp == 'S':
        arquivo.criarArquivo(arq)
        sleep(0.7)

    elif resp == 'N':
        print('Ok! Finalizando programa...')
        sleep(1)
        interface.titulo('Programa finalizado!!')
        exit()

else:
    print('\033[32mArquivo encontrado!!\033[m')
    sleep(0.7)

while True:
    esco = interface.menu('VER PESSOAS CADASTRADAS', 'CADASTRAR PESSOA', 'SAIR DO PROGRAMA')
    if esco == 1:
        interface.titulo('PESSOAS CADASTRADAS')
        arquivo.lerArquivo(arq)

    elif esco == 2:
        interface.titulo('CADASTRAR PESSOA')
        nome = str(input('Informe o nome da pessoa: ')).strip()
        idade = dado.leiaInt('Informe a idade da pessoa: ')
        dado.cadastrar(arq, nome, idade)

    else:
        print('Opção 3')
        break
    sleep(1)
interface.titulo('PROGRAMA FINALIZADO!!')
