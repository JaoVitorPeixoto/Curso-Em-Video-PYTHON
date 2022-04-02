print('======== DESAFIO 87 ========')
print('')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe o valor da posição [{l},{c}]: '))

somapar = somacol = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]

        if c == 2:
            somacol += matriz[l][c]

        if l == 1:
            maiorvalor = max(matriz[l])

print('-='*30)
print('A sua matriz é:')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end=' ')
    print()

print('--'*30)
print(f'A soma dos valores pares é \033[33m{somapar}\033[m;')
print(f'A soma dos valores da terceira coluna é \033[33m{somacol}\033[m;')
print(f'O maior valor da segunda linha é \033[33m{maiorvalor}\033[m.')
print('-='*30)
