print('======== DESAFIO 68 ========')
print('')

from random import randint
from time import sleep

titulo = '\033[31mPAR\033[m OU \033[34mÍMPAR\033[m'
print('\033[34m-\033[31m=\033[m'*30)
print(f'{titulo:^74}')
print('\033[34m-\033[31m=\033[m'*30)

vit = 0
while True:
    computador = randint(0, 20)
    num = int(input('Qual número você quer? '))
    soma = computador + num
    r = soma % 2
    escolha = str(input('\033[31mPar\033[m ou \033[34mÍmpar\033[m? [\033[31mP\033[m/\033[34mI\033[m]' )).upper().strip()[0]
    while escolha not in 'PI':
        escolha = str(input('INFORME CORRETAMENTE!!! \033[31mPar\033[m ou \033[34mÍmpar\033[m? [\033[31mP\033[m/\033[34mI\033[m] ')).upper().strip()[0]
    print('\033[34m-\033[31m=\033[m'*30)

    print('\033[31mPAR\033[m')
    sleep(1)
    print('OU')
    sleep(1)
    print('\033[34mÍMPAR!!\033[m')
    print('\033[34m-\033[31m-\033[m' * 30)

    if r == 0:
        ou = '\033[31mPAR!!\033[m'
        if escolha in 'P':
            vit += 1
            print(f'\033[32mVOCÊ GANHOU!!!\033[m O computador escolheu \033[33m{computador}\033[m e você \033[33m{num}\033[m, tendo um total de \033[33m{soma}\033[m deu {ou}')
            sleep(1)
        else:
            print(f'\033[31mGAME OVER!!!\033[m O computador escolheu \033[33m{computador}\033[m e você \033[33m{num}\033[m, tendo um total de \033[33m{soma}\033[m deu {ou}')
            sleep(1)
            break

    elif r == 1:
        ou = '\033[34mÍMPAR!!\033[m'
        if escolha in 'IÍ':
            vit += 1
            print( f'\033[32mVOCÊ GANHOU!!!\033[m O computador escolheu \033[33m{computador}\033[m e você \033[33m{num}\033[m, tendo um total de \033[33m{soma}\033[m deu {ou}')
            sleep(1)
        else:

            print(f'\033[31mGAME OVER!!!\033[m O computador escolheu \033[33m{computador}\033[m e você \033[33m{num}\033[m, tendo um total de \033[33m{soma}\033[m deu {ou}')
            sleep(1)
            break

    print('\033[34m-\033[31m-\033[m' * 30)

print('\033[34m-\033[31m=\033[m'*30)
print(f'A quantidade de \033[32mVITÓRIAS\033[m foi \033[32m{vit}\033[m.')

