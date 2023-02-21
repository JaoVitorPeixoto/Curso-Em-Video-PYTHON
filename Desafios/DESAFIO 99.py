from time import sleep

def maior(*num):
    print('Analizando os valores...')
    sleep(1)
    print('--'*30)
    maior = 0
    for c in range(0, len(num)):
        print(num[c], end=' ')
        if c == 0:
            maior = num[c]
        else:
            if num[c] > maior:
                maior = num[c]
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi o {maior}.')
    print('-='*30)


# Programa principal >>>>>>>>
print('======== DESAFIO 99 ========')
print('')

maior(5, 1, 8, 2, 10, 9, 55, 7, 3)
maior(-1, -100, -200, -2)
maior()
