print('======== DESAFIO 28 ========')
print('')
from time import sleep
from random import randint
print('==========ADIVINHE O NÚMERO==========')

num = randint(0, 5)
print('-=-'*20)
print('Tente adivinhar no número que o computador está "pensando"!!')
print('-=-'*20)
adv = int(input('Escolha um número de 0 a 5: '))

print('PROCESSANDO...')
sleep(2)

print('-=-'*20)
if adv == num:
    print('Você acertou, parabéns!!!')
else:
    print(f'Você errou... o número certo era {num}.')
print('>>>>Fim<<<<')
