print('======== DESAFIO 74 ========')
print('')

from random import randint

numeros = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))

menor = maior = 0

print(f'Os números sorteados foram: {numeros}')
print(f'O maior número foi \033[32m{max(numeros)}\033[m, e o menor número foi \033[31m{min(numeros)}\033[m.')
