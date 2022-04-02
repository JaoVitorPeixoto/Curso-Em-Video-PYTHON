print('======== DESAFIO 79 ========')
print('')

from time import sleep

valores = []

while True:
    v = int(input('Informe um valor: '))
    if v in valores:
        print(f'{v} já existe na lista, não vou adicionar...')
    else:
        print(f'{v} adicionado com sucesso!!!')
        valores.append(v)

    print('-='*30)
    esco = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while esco not in 'SN':
        esco = str(input('ERRO! Informe corretamente, quer continuar? [S/N]')).upper().strip()[0]
    print('-='*30)

    if esco == 'N':
        print('Ok! Finalizando...')
        sleep(1)
        break

valores.sort()
print(f'Os valores unicos digitados em ordem crescente é: {valores}')