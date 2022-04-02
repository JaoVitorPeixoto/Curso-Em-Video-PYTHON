print('======== DESAFIO 58 ========')
print('')

from time import sleep
from random import randint
print('==========ADIVINHE O NÚMERO==========')

num = randint(0, 10)
print('-=-'*20)
print('Tente adivinhar no número que o computador está \033[34m"pensando"\033[m!!')
print('-=-'*20)
adv = int(input('Escolha um número de \033[33m0\033[m a \033[33m10\033[m: '))

tentativas = 1
while adv != num:
    print('\033[33mPROCESSANDO...\033[m')
    sleep(0.7)
    print(' ')
    if adv > num:
        print(f'\033[31mVocê errou...\033[mÉ um número \033[33mMENOR\033[m que \033[33m{adv}\033[m...Tente novamente.')
        adv = int(input('Escolha: '))

    elif adv < num:
        print(f'\033[31mVocê errou...\033[mÉ um número \033[33mMAIOR\033[m que \033[33m{adv}\033[m...Tente novamente.')
        adv = int(input('Escolha: '))
    tentativas += 1

print('')
print(f'\033[32mVocê acertou!!!\033[m o número escolhido foi \033[33m{num}\033[m, e a quantidade de tentativas foi \033[33m{tentativas}\033[m')
print('\033[36m>>>>Fim<<<<\033[m')
