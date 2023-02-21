print('======== DESAFIO 81 ========')
print('')

from time import sleep

valores = []

while True:
    valores.append(int(input('Informe um número: ')))

    esco = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while esco not in 'SN':
      esco = str(input('ERRO!! Informe corretamente, quer continuar? [S/N]')).upper().strip()[0]
    print('-='*30)

    if esco == 'N':
        print('Ok! Finalizando programa...')
        sleep(1)
        break

print('-='*30)
valores.sort(reverse = True)

print(f'A quantidade de valores digitados foi {len(valores)};')
print(f'A lista em ordem decrescente é: {valores};')
print(f'O valor 5 faz parte da lista e apareceu {valores.count(5)} vez(es)' if (5 in valores) else 'O valor 5 não faz parte da lista!!')
