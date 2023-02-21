print('======== DESAFIO 33 ========')
print('')

print('==========INFORME 3 NÚMEROS PARA SABER QUAL É O MAIOR E QUAL É O MENOR==========')

n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))

if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print(f'O maior número é {n1:.2f}.')
            print(f'{n3:.2f} é o menor número.')
        else:
            print(f'O maior número é {n1:.2f}')
            print(f'{n2:.2f} é o menor número.')
    else:
        print(f'O maior número é {n3:.2f}')
        print(f'{n2:.2f} é o menor número.')
else:
    if n2 > n3:
        if n1 > n3:
            print(f'O maior número é {n2:.2f}.')
            print(f'{n3:.2f} é o menor número.')
        else:
            print(f'O maior número é{n2:.2f}.')
            print(f'{n1:.2f} é o menor número.')
    else:
        print(f'O maior número é {n3:.2f}.')
        print(f'{n1:.2f} é o menor número.')