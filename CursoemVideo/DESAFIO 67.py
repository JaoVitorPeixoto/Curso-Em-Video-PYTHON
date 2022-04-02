print('======== DESAFIO 67 ========')
print('')

from time import sleep

print(f'{"TABUADA":=^37}')

c = 1
while True:
    num = int(input('Informe o valor que deseja saber a sua TABUADA \033[33m[ digite um número negativo para parar ]\033[m: '))

    if num < 0:
        break

    print('-='*30)

    for c in range(1, 11):
        print(f'  {num:2} x {c:2} = {num * c:2} ')

    print('-='*30)

print('-='*30)
print('Finalizando programa...', end=' ')
sleep(2)
print('Programa finalizado com sucesso!!')