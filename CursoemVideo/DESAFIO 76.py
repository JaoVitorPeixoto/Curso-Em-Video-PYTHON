print('======== DESAFIO 76 ========')
print('')

produtos = ('Leite', 5.50,
            'Café', 4.25,
            'Lápis', 1,
            'Caneta', 2,
            'Mochila', 70,
            'Caderno', 20,
            'Estojo', 10,
            'Borracha', 2)

print('--'*21)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('--'*21)

for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    else:
        print(f'R$  {produtos[c]:>5.2f}')

print('--'*21)