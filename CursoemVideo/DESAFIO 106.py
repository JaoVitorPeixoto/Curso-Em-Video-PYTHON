c = ('\033[m'       # 0 - sem cor
     , '\033[0;30;41m' # 1 - vermelho
     , '\033[0;30;42m' # 2 - verde
     , '\033[0;30;43m',# 3 - amarelo
     '\033[0;30;44m'   # 4 - azul
     )


def escreva(txt, cor=0):
    n = len(txt) + 4
    print(f'{c[cor]}', end='')
    print(f'~'*(n))
    print(f'{txt:^{n}}')
    print('~'*(n))
    print(f'{c[0]}', end='')


def pyHelp():

    while True:
        escreva('Sistema de ajuda PyHelp', 2)
        comando = str(input('Função ou biblioteca > ')).lower().strip()
        if comando == 'fim':
            break
        escreva(f'Acessando o manual de comando \'{comando}\'', 4)
        print('\033[7m', end='')
        help(comando)
        print('\033[m')

# Programa principal >>>>>>>>
print('======== DESAFIO 105 ========')
print('')

pyHelp()