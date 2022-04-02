print('======== DESAFIO 45 ========')
print('')

from time import sleep
from random import randint

print('''\033[7m=====JOKENPÔ=====\033[m
\033[7m[ 0 ] = PEDRA    \033[m
\033[7m[ 1 ] = PAPEL    \033[m
\033[7m[ 2 ] = TESOURA  \033[m''')
print('')

pc = randint(0, 2)
num = int(input('Informe entre 0, 1 e 2 para decidir se quer \033[31mpedra\033[m, \033[32mpapel\033[m ou \033[34mtesoura\033[m respectivamente: '))
formas = ['\033[31mPEDRA\033[m', '\033[32mPAPEL\033[m', '\033[34mTESOURA\033[m']
print('-='*30)

print('\033[36mJO\033[m')
sleep(1)
print('\033[36mKEN\033[m')
sleep(1)
print('\033[36mPÔ!!!\033[m')
print('-='*30)

if num == pc:
    print(f'\033[33mEMPATE!!\033[m')
    print(f'Você escolheu {formas[num]}, e o computador também escolheu {formas[pc]}')

elif num == 0 and pc == 2:
    print('\033[32mVOCÊ GANHOU!!\033[m')
    print(f'Você escolheu {formas[num]}, e o computador {formas[pc]}')

elif num == 1 and pc == 0:
    print(f'\033[32mVOCÊ GANHOU!!\033[m')
    print(f'Você escolheu {formas[num]}, e o computador {formas[pc]}')

elif num == 2 and pc == 1:
    print('\033[32mVOCÊ GANHOU!!\033[m')
    print(f'Você escolheu {formas[num]}, e o computador {formas[pc]}')

else:
    print('\033[31mVOCÊ PERDEU!!\033[m')
    print(f'Você escolheu {formas[num]}, e o computador {formas[pc]}')
print('-='*30)