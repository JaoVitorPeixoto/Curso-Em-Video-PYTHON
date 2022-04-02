print('======== DESAFIO 82 ========')
print('')

from time import sleep


valores =  []
pares = []
impares = []


while True:
    n = int(input('Informe um número: '))
    valores.append(n)

    esco = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while esco not in 'SN':
        esco = str(input('ERRO!! Informe corretamente, quer continuar? [S/N]')).upper().strip()[0]
    print('-=' * 30)

    if esco == 'N':
        print('Ok! Finalizando programa...')
        print('-='*30)
        sleep(1)
        break

for c in valores:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print(f'Os valores digitados foram: {valores};')
print(f'Os valores \033[31mPARES\033[m são: {pares}')
print(f'Os valores \033[34mÍMPARES\033[m são: {impares}')
