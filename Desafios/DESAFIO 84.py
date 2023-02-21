print('======== DESAFIO 84 ========')
print('')

from time import sleep

dados = []
pessoas = []
maior = menor = 0
cont = 1
while True:
    print('-='*30)
    dados.append(str(input(f'Informe o nome da {cont}ª pessoa: ')).strip())
    dados.append(float(input(f'Informe o peso da {cont}ª pessoa: ')))

    if cont == 1:
        menor = maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    print('--'*30)
    esco = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while esco not in 'NS':
        esco = str(input('ERRO!! Informe corretamente, quer continuar? [S/N]')).upper().strip()[0]
    if esco == 'N':
        print('Ok!! Finalizando programa...')
        sleep(1)
        print('-='*30)
        break
    cont += 1

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior:.2f}Kg. Peso de ', end='')
for nom, pes in pessoas:
    if maior == pes:
        print(f'[{nom}]', end=' ')

print(f'\nO menor peso foi {menor:.2f}Kg. Peso de ', end='')
for nom, pes in pessoas:
    if menor == pes:
        print(f'[{nom}]', end=' ')